# src/main.py
"""
Main script for auto-wiki system using GitHub Issues as a processing queue.
"""

import json
import os
import sys
from pathlib import Path
from typing import List

import fire
from loguru import logger

from .wiki_manager import WikiManager


def setup_logger(log_level: str = "INFO"):
    """Set up the logger with specified log level."""
    logger.remove()  # Remove default handler
    logger.add(
        sink=lambda msg: print(msg),
        level=log_level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{file}:{line}</cyan> - <level>{message}</level>",
    )


def process_file(
    file_path: str,
    token: str = None,
    repo: str = None,
    wiki_dir: str = "wiki",
    system_prompt_path: str = "prompts/system_prompt.md",
):
    """
    Process a markdown file to identify wiki links and create tasks.
    
    Args:
        file_path: Path to markdown file
        token: GitHub token (can also use GITHUB_TOKEN env var)
        repo: GitHub repository (can also use GITHUB_REPOSITORY env var)
        wiki_dir: Directory to store wiki files
        system_prompt_path: Path to system prompt file
    """
    setup_logger()
    
    # Get token and repo from environment if not provided
    token = token or os.environ.get("GITHUB_TOKEN")
    if not token:
        logger.error("GitHub token not provided")
        sys.exit(1)
    
    repo = repo or os.environ.get("GITHUB_REPOSITORY")
    if not repo:
        logger.error("GitHub repository not provided")
        sys.exit(1)
    
    try:
        # Convert paths
        file_path = Path(file_path)
        
        # Create wiki manager
        manager = WikiManager(
            token=token,
            repo=repo,
            wiki_dir=wiki_dir,
            system_prompt_path=system_prompt_path
        )
        
        # Process the file
        if file_path.exists():
            tasks = manager.process_markdown_file(file_path)
            logger.info(f"Created {len(tasks)} tasks for {file_path}")
            
            # Print summary
            print(json.dumps({
                "file": str(file_path),
                "tasks_created": len(tasks),
                "tasks": tasks
            }, indent=2))
        else:
            logger.error(f"File not found: {file_path}")
            sys.exit(1)
    
    except Exception as e:
        logger.exception(f"Error: {str(e)}")
        sys.exit(1)


def process_changed_files(
    files: List[str],
    token: str = None,
    repo: str = None,
    wiki_dir: str = "wiki",
    system_prompt_path: str = "prompts/system_prompt.md",
):
    """
    Process a list of changed files to create wiki content tasks.
    
    Args:
        files: List of file paths to process
        token: GitHub token (can also use GITHUB_TOKEN env var)
        repo: GitHub repository (can also use GITHUB_REPOSITORY env var)
        wiki_dir: Directory to store wiki files
        system_prompt_path: Path to system prompt file
    """
    setup_logger()
    
    # Get token and repo from environment if not provided
    token = token or os.environ.get("GITHUB_TOKEN")
    if not token:
        logger.error("GitHub token not provided")
        sys.exit(1)
    
    repo = repo or os.environ.get("GITHUB_REPOSITORY")
    if not repo:
        logger.error("GitHub repository not provided")
        sys.exit(1)
    
    try:
        # Create wiki manager
        manager = WikiManager(
            token=token,
            repo=repo,
            wiki_dir=wiki_dir,
            system_prompt_path=system_prompt_path
        )
        
        # Process the files
        result = manager.process_changed_files(files)
        logger.info(f"Processed {result['processed_files']} files, created {result['total_tasks']} tasks")
        
        # Print summary
        print(json.dumps(result, indent=2))
    
    except Exception as e:
        logger.exception(f"Error: {str(e)}")
        sys.exit(1)


def check_wiki_page(
    topic: str,
    token: str = None,
    repo: str = None,
    wiki_dir: str = "wiki",
):
    """
    Check the status of a wiki page.
    
    Args:
        topic: Topic to check
        token: GitHub token (can also use GITHUB_TOKEN env var)
        repo: GitHub repository (can also use GITHUB_REPOSITORY env var)
        wiki_dir: Directory to store wiki files
    """
    setup_logger()
    
    # Get token and repo from environment if not provided
    token = token or os.environ.get("GITHUB_TOKEN")
    if not token:
        logger.error("GitHub token not provided")
        sys.exit(1)
    
    repo = repo or os.environ.get("GITHUB_REPOSITORY")
    if not repo:
        logger.error("GitHub repository not provided")
        sys.exit(1)
    
    try:
        # Create wiki manager
        manager = WikiManager(
            token=token,
            repo=repo,
            wiki_dir=wiki_dir
        )
        
        # Check page status
        status = manager.check_wiki_page_status(topic)
        logger.info(f"Wiki page status: {status['status']}")
        
        # Print status
        print(json.dumps(status, indent=2))
    
    except Exception as e:
        logger.exception(f"Error: {str(e)}")
        sys.exit(1)


def main():
    """Entry point for the command-line interface."""
    fire.Fire({
        "process_file": process_file,
        "process_changed_files": process_changed_files,
        "check_wiki_page": check_wiki_page,
    })


if __name__ == "__main__":
    main()
