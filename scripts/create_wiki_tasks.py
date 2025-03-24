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


def clean_links(wikilinks, collect_aliases=False):
    """
    Canonicalize aliases, standardize case.
    
    Args:
        wikilinks: List of wiki links
        collect_aliases: Whether to collect aliases (not implemented)
        
    Returns:
        List of cleaned wiki links
    """
    if collect_aliases:
        raise NotImplementedError("Alias collection not implemented yet")
    
    outv = []
    for link in wikilinks:
        if '|' in link:
            try:
                link, alias = link.split('|')
            except:
                print(link)
                raise
        outv.append(link.lower())
    return outv


def get_wikilinks(text):
    """
    Extract wiki links from text.
    
    Args:
        text: Text to extract links from
        
    Returns:
        List of wiki links
    """
    links_pat = re.compile(r"\[\[(.+?)\]\]")
    matches = re.findall(links_pat, text)
    if not matches:
        return []
    
    matches = clean_links(matches)
    logger.info(f"Links detected: {matches}")
    return matches


def find_missing_wiki_pages(
    source_path: Path,
    root_dir: Path
) -> set[str]:
    """
    Find wiki links in a file that don't have corresponding wiki pages.
    
    Args:
        source_path: Path to the markdown file
        root_dir: Root directory for content
        
    Returns:
        Set of wiki link titles that don't have corresponding files
    """
    logger.info(f"Analyzing file: {source_path}")
    
    # Read the markdown file
    try:
        content = source_path.read_text(encoding="utf-8")
    except Exception as e:
        logger.error(f"Error reading file {source_path}: {e}")
        return set()
    
    # Extract wiki links
    links = get_wikilinks(content)
    logger.info(f"Found {len(links)} wiki links in {source_path}")
    
    # Filter out links that already have corresponding files
    missing_pages = set()
    for link in links:
        # Check for file with the same name anywhere in the root directory
        # (could be in wiki/ or any other subdirectory)
        matching_files = list(root_dir.glob(f"**/{link}.md"))
        
        if not matching_files:
            missing_pages.add(link)
    
    logger.info(f"Found {len(missing_pages)} missing wiki pages")
    return missing_pages


def create_wiki_task(
    topic: str,
    token: str = None,
    repo: str = None,
    output_dir: str = "wiki",
    system_prompt_path: str = "prompts/system_prompt.md",
) -> Dict[str, Any]:
    """
    Create a gh-store object for a wiki page task.
    
    Args:
        topic: Topic to create task for
        token: GitHub token (defaults to GITHUB_TOKEN env var)
        repo: GitHub repository (defaults to GITHUB_REPOSITORY env var)
        output_dir: Directory where generated content will be stored
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
    
    # Initialize the store
    store = GitHubStore(token=token, repo=repo)
    
    # Task configuration for generating wiki page
    task_config = {
        "operator": "generate_wiki",
        "kwargs": {
            "topic": topic,
            "output_dir": output_dir,
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
    root_dir: str = ".",
    output_dir: str = "wiki",
    system_prompt_path: str = "prompts/system_prompt.md",
) -> Dict[str, Any]:
    """
    Process a markdown file to find wiki links and create tasks.
    
    Args:
        file_path: Path to markdown file
        token: GitHub token (can also use GITHUB_TOKEN env var)
        repo: GitHub repository (can also use GITHUB_REPOSITORY env var)
        root_dir: Root directory to search for existing files
        output_dir: Directory where generated content will be stored
        system_prompt_path: Path to system prompt file
        
    Returns:
        Dictionary with processing results
    """
    logger.info(f"Processing file: {file_path}")
    
    # Ensure output directory exists
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True, parents=True)
    
    # Get file path and root directory
    file_path = Path(file_path)
    root_dir = Path(root_dir)
    
    if not file_path.exists():
        logger.error(f"File not found: {file_path}")
        return {"file": str(file_path), "status": "error", "error": "File not found"}
    
    missing_pages = find_missing_wiki_pages(file_path, root_dir)
    
    # Create tasks for missing pages
    results = []
    for topic in missing_pages:
        result = create_wiki_task(
            topic=topic,
            token=token,
            repo=repo,
            output_dir=output_dir,
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
    root_dir: str = ".",
    output_dir: str = "wiki",
    system_prompt_path: str = "prompts/system_prompt.md",
) -> Dict[str, Any]:
    """
    Process multiple files to find wiki links and create tasks.
    
    Args:
        file_paths: List of file paths to process
        token: GitHub token
        repo: GitHub repository
        root_dir: Root directory to search for existing files
        output_dir: Directory where generated content will be stored
        system_prompt_path: Path to system prompt
        
    Returns:
        Dictionary with processing results
    """
    logger.info(f"Processing {len(file_paths)} files")
    logger.info(f"{file_paths}")
    
    # Process each file
    results = []
    for file_path in file_paths:
        logger.info(f"Processing {file_path}...")
        if file_path.lower().endswith(('.md', '.markdown')):
            result = process_file(
                file_path=file_path,
                token=token,
                repo=repo,
                root_dir=root_dir,
                output_dir=output_dir,
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
