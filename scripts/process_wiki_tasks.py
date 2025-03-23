# scripts/process_wiki_tasks.py
"""
Process wiki tasks from gh-store and generate content.
"""

import json
import os
import subprocess
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime, timezone

import fire
from loguru import logger
from gh_store.core.store import GitHubStore


def get_pending_wiki_tasks(
    token: str = None,
    repo: str = None,
    wiki_dir: str = "wiki",
    limit: int = 10,
) -> List[Dict[str, Any]]:
    """
    Get a list of pending wiki tasks from gh-store.
    
    Args:
        token: GitHub token (can also use GITHUB_TOKEN env var)
        repo: GitHub repository (can also use GITHUB_REPOSITORY env var)
        wiki_dir: Wiki directory
        limit: Maximum number of tasks to return
        
    Returns:
        List of pending wiki tasks
    """
    # Get token and repo from environment if not provided
    token = token or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise ValueError("GitHub token not provided")
    
    repo = repo or os.environ.get("GITHUB_REPOSITORY")
    if not repo:
        raise ValueError("GitHub repository not provided")
    
    # Initialize the store
    store = GitHubStore(token=token, repo=repo)
    
    # Get all objects
    all_objects = store.list_all()
    logger.info(f"Found {len(all_objects)} objects in store")
    
    # Filter for wiki tasks
    wiki_tasks = []
    for object_id, obj in all_objects.items():
        data = obj.data
        
        # Check if this is a wiki task
        if (isinstance(data, dict) and 
            data.get("operator") == "generate_wiki" and
            isinstance(data.get("kwargs"), dict) and
            "topic" in data.get("kwargs", {})):
            
            # Check if wiki file already exists
            topic = data["kwargs"]["topic"]
            wiki_file = Path(wiki_dir) / f"{topic}.md"
            
            if not wiki_file.exists():
                wiki_tasks.append({
                    "object_id": object_id,
                    "task_config": data,
                    "status": data.get("status", "pending"),
                    "meta": {
                        "created_at": obj.meta.created_at,
                        "updated_at": obj.meta.updated_at,
                        "version": obj.meta.version
                    }
                })
    
    # Sort by created date (oldest first) and limit
    wiki_tasks.sort(key=lambda x: x["meta"]["created_at"])
    wiki_tasks = wiki_tasks[:limit]
    
    logger.info(f"Found {len(wiki_tasks)} pending wiki tasks")
    return wiki_tasks


def process_wiki_task(
    object_id: str,
    task_config: Dict[str, Any],
    token: str = None,
    repo: str = None,
) -> Dict[str, Any]:
    """
    Process a wiki task by executing its operator.
    
    Args:
        object_id: Object ID (topic name)
        task_config: Task configuration dictionary
        token: GitHub token
        repo: GitHub repository
        
    Returns:
        Dictionary with processing results
    """
    logger.info(f"Processing wiki task: {object_id}")
    
    # Verify this is a wiki task
    if task_config.get("operator") != "generate_wiki":
        logger.warning(f"Not a wiki task: {object_id}")
        return {"topic": object_id, "status": "skipped", "reason": "Not a wiki task"}
    
    # Get task parameters
    kwargs = task_config.get("kwargs", {})
    topic = kwargs.get("topic")
    wiki_dir = kwargs.get("wiki_dir", "wiki")
    
    if not topic:
        logger.error(f"Missing topic in task: {object_id}")
        return {"topic": object_id, "status": "error", "error": "Missing topic parameter"}
    
    # Check if wiki file already exists
    wiki_path = Path(wiki_dir) / f"{topic}.md"
    if wiki_path.exists():
        logger.info(f"Wiki file already exists: {wiki_path}")
        return {"topic": topic, "status": "exists", "file_path": str(wiki_path)}
    
    # Process the task
    try:
        # Call process_task.py to generate content
        task_json = json.dumps(task_config)
        
        result = subprocess.run(
            ["python", "scripts/process_task.py", "--config", task_json],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Check if wiki file was created
        if wiki_path.exists():
            logger.info(f"Wiki file created: {wiki_path}")
            
            # Update task status in gh-store
            store = GitHubStore(token=token, repo=repo)
            store.update(object_id, {
                "status": "completed",
                "completed_at": datetime.now(timezone.utc).isoformat()
            })
            
            return {
                "topic": topic, 
                "status": "created", 
                "file_path": str(wiki_path),
                "output": result.stdout[:500]  # Truncate long output
            }
        else:
            logger.warning(f"Task completed but wiki file not found: {wiki_path}")
            
            # Update task status in gh-store
            store = GitHubStore(token=token, repo=repo)
            store.update(object_id, {
                "status": "failed",
                "error": "Task completed but wiki file not found",
                "failed_at": datetime.now(timezone.utc).isoformat()
            })
            
            return {
                "topic": topic,
                "status": "error",
                "error": "Task completed but wiki file not found",
                "output": result.stdout
            }
    except subprocess.CalledProcessError as e:
        logger.error(f"Error processing task: {e.stderr}")
        
        # Update task status in gh-store
        store = GitHubStore(token=token, repo=repo)
        store.update(object_id, {
            "status": "failed",
            "error": e.stderr,
            "failed_at": datetime.now(timezone.utc).isoformat()
        })
        
        return {"topic": topic, "status": "error", "error": e.stderr}
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        
        # Update task status in gh-store
        store = GitHubStore(token=token, repo=repo)
        store.update(object_id, {
            "status": "failed",
            "error": str(e),
            "failed_at": datetime.now(timezone.utc).isoformat()
        })
        
        return {"topic": topic, "status": "error", "error": str(e)}


def process_all_tasks(
    token: str = None,
    repo: str = None,
    wiki_dir: str = "wiki",
    limit: int = 10,
) -> Dict[str, Any]:
    """
    Process all pending wiki tasks from gh-store.
    
    Args:
        token: GitHub token (can also use GITHUB_TOKEN env var)
        repo: GitHub repository (can also use GITHUB_REPOSITORY env var)
        wiki_dir: Wiki directory
        limit: Maximum number of tasks to process in one run
        
    Returns:
        Dictionary with processing results
    """
    logger.info(f"Processing pending wiki tasks (limit: {limit})")
    
    # Get token and repo from environment if not provided
    token = token or os.environ.get("GITHUB_TOKEN")
    if not token:
        return {"status": "error", "error": "GitHub token not provided"}
    
    repo = repo or os.environ.get("GITHUB_REPOSITORY")
    if not repo:
        return {"status": "error", "error": "GitHub repository not provided"}
    
    # Get pending wiki tasks
    try:
        wiki_tasks = get_pending_wiki_tasks(token, repo, wiki_dir, limit)
    except Exception as e:
        logger.error(f"Error getting pending tasks: {str(e)}")
        return {"status": "error", "error": str(e)}
    
    if not wiki_tasks:
        logger.info("No pending wiki tasks found")
        return {"status": "completed", "total_tasks": 0, "message": "No pending tasks"}
    
    # Process each task
    results = []
    for task in wiki_tasks:
        result = process_wiki_task(
            object_id=task["object_id"],
            task_config=task["task_config"],
            token=token,
            repo=repo
        )
        results.append(result)
    
    # Count successes and failures
    successes = len([r for r in results if r["status"] == "created"])
    failures = len([r for r in results if r["status"] == "error"])
    
    return {
        "status": "completed",
        "total_tasks": len(wiki_tasks),
        "successes": successes,
        "failures": failures,
        "results": results
    }


def main():
    """Command-line interface."""
    fire.Fire({
        "get_tasks": get_pending_wiki_tasks,
        "process": process_all_tasks,
    })


if __name__ == "__main__":
    main()
