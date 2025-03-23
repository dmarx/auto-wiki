# scripts/create_wiki_tasks.py
"""
Create tasks in gh-store for wiki pages that need to be generated.
"""

import json
import os
import re
from pathlib import Path
from typing import Set, List, Dict, Any

import fire
from loguru import logger
from gh_store.core.store import GitHubStore
from gh_store.core.exceptions import ObjectNotFound


def extract_wiki_links(content: str) -> set[str]:
    """
    Extract all unique wiki links from content.
    
    Args:
        content: The markdown content to parse
        
    Returns:
        A set of unique wiki link titles
    """
    pattern = r"\[\[(.*?)\]\]"
    matches = re.findall(pattern, content)
    return set(matches)


def find_missing_wiki_pages(
    source_path: Path,
    wiki_dir: Path
) -> set[str]:
    """
    Find wiki links in a file that don't have corresponding wiki pages.
    
    Args:
        source_path: Path to the markdown file
        wiki_dir: Path to the directory containing wiki pages
        
    Returns:
        Set of wiki link titles that don't have corresponding files
    """
    logger.info(f"Analyzing file: {source_path}")
    
    # Ensure wiki directory exists
    wiki_dir.mkdir(exist_ok=True, parents=True)
    
    # Read the markdown file
    try:
        content = source_path.read_text(encoding="utf-8")
    except Exception as e:
        logger.error(f"Error reading file {source_path}: {e}")
        return set()
    
    # Extract wiki links
    links = extract_wiki_links(content)
    logger.info(f"Found {len(links)} wiki links in {source_path}")
    
    # Filter out links that already have wiki pages
    missing_pages = set()
    for link in links:
        wiki_file = wiki_dir / f"{link}.md"
        if not wiki_file.exists():
            missing_pages.add(link)
    
    logger.info(f"Found {len(missing_pages)} missing wiki pages")
    return missing_pages


def create_wiki_task(
    topic: str,
    token: str = None,
    repo: str = None,
    wiki_dir: str = "wiki",
    system_prompt_path: str = "prompts/system_prompt.md",
) -> Dict[str, Any]:
    """
    Create a gh-store object for a wiki page task.
    
    Args:
        topic: Topic to create task for
        token: GitHub token (defaults to GITHUB_TOKEN env var)
        repo: GitHub repository (defaults to GITHUB_REPOSITORY env var)
        wiki_dir: Wiki directory
        system_prompt_path: Path to system prompt
        
    Returns:
        Dictionary with result information
    """
    # Get token and repo from environment if not provided
    token = token or os.environ.get("GITHUB_TOKEN")
    if not token:
        logger.error("GitHub token not provided")
        return {"topic": topic, "status": "error", "error": "GitHub token not provided"}
    
    repo = repo or os.environ.get("GITHUB_REPOSITORY")
    if not repo:
        logger.error("GitHub repository not provided")
        return {"topic": topic, "status": "error", "error": "GitHub repository not provided"}
    
    # Check if wiki file already exists
    wiki_path = Path(wiki_dir) / f"{topic}.md"
    if wiki_path.exists():
        logger.info(f"Wiki page already exists: {wiki_path}")
        return {"topic": topic, "status": "exists", "file_path": str(wiki_path)}
    
    # Initialize the store
    store = GitHubStore(token=token, repo=repo)
    
    # Task configuration for generating wiki page
    task_config = {
        "operator": "generate_wiki",
        "kwargs": {
            "topic": topic,
            "wiki_dir": wiki_dir,
            "system_prompt_path": system_prompt_path
        },
        "status": "pending"
    }
    
    # Create gh-store object
    try:
        # First check if object already exists
        try:
            store.get(topic)
            # Object exists
            logger.info(f"Task already exists for topic: {topic}")
            return {"topic": topic, "status": "existing_task", "object_id": topic}
        except ObjectNotFound:
            # Object doesn't exist, create it
            obj = store.create(topic, task_config)
            logger.info(f"Created task for topic: {topic}")
            return {"topic": topic, "status": "created", "object_id": topic}
    except Exception as e:
        logger.error(f"Error creating task: {str(e)}")
        return {"topic": topic, "status": "error", "error": str(e)}


def process_file(
    file_path: str,
    token: str = None,
    repo: str = None,
    wiki_dir: str = "wiki",
    system_prompt_path: str = "prompts/system_prompt.md",
) -> Dict[str, Any]:
    """
    Process a markdown file to find wiki links and create tasks.
    
    Args:
        file_path: Path to markdown file
        token: GitHub token (can also use GITHUB_TOKEN env var)
        repo: GitHub repository (can also use GITHUB_REPOSITORY env var)
        wiki_dir: Directory to store wiki files
        system_prompt_path: Path to system prompt file
        
    Returns:
        Dictionary with processing results
    """
    logger.info(f"Processing file: {file_path}")
    
    # Ensure directories exist
    wiki_dir_path = Path(wiki_dir)
    wiki_dir_path.mkdir(exist_ok=True, parents=True)
    
    # Get missing wiki pages
    file_path = Path(file_path)
    if not file_path.exists():
        logger.error(f"File not found: {file_path}")
        return {"file": str(file_path), "status": "error", "error": "File not found"}
    
    missing_pages = find_missing_wiki_pages(file_path, wiki_dir_path)
    
    # Create tasks for missing pages
    results = []
    for topic in missing_pages:
        result = create_wiki_task(
            topic=topic,
            token=token,
            repo=repo,
            wiki_dir=wiki_dir,
            system_prompt_path=system_prompt_path
        )
        results.append(result)
    
    # Return summary
    return {
        "file": str(file_path),
        "total_links": len(missing_pages),
        "tasks_created": len([r for r in results if r["status"] == "created"]),
        "results": results
    }


def process_changed_files(
    file_paths: List[str],
    token: str = None,
    repo: str = None,
    wiki_dir: str = "wiki",
    system_prompt_path: str = "prompts/system_prompt.md",
) -> Dict[str, Any]:
    """
    Process multiple files to find wiki links and create tasks.
    
    Args:
        file_paths: List of file paths to process
        token: GitHub token
        repo: GitHub repository
        wiki_dir: Wiki directory
        system_prompt_path: Path to system prompt
        
    Returns:
        Dictionary with processing results
    """
    logger.info(f"Processing {len(file_paths)} files")
    
    # Process each file
    results = []
    for file_path in file_paths:
        if file_path.lower().endswith(('.md', '.markdown')):
            result = process_file(
                file_path=file_path,
                token=token,
                repo=repo,
                wiki_dir=wiki_dir,
                system_prompt_path=system_prompt_path
            )
            results.append(result)
    
    # Summarize results
    total_links = sum(r.get("total_links", 0) for r in results)
    total_created = sum(r.get("tasks_created", 0) for r in results)
    
    return {
        "total_files": len(file_paths),
        "processed_files": len(results),
        "total_links": total_links,
        "total_tasks_created": total_created,
        "results": results
    }


def main():
    """Command-line interface."""
    fire.Fire({
        "process_file": process_file,
        "process_changed_files": process_changed_files,
    })


if __name__ == "__main__":
    main()
