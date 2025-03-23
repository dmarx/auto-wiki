# src/wiki_manager.py
"""
Manager for handling wiki content generation using GitHub Issues as a queue.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Set

from loguru import logger
from github import Github

from .wiki_parser import extract_wiki_links, find_missing_wiki_pages


class WikiManager:
    """
    Manager for handling wiki content generation through GitHub Issues.
    Uses gh-store conventions underneath for state management.
    """
    
    def __init__(
        self,
        token: str,
        repo: str,
        wiki_dir: str = "wiki",
        system_prompt_path: str = "prompts/system_prompt.md",
    ):
        """
        Initialize the wiki manager.
        
        Args:
            token: GitHub token
            repo: Repository name (owner/repo)
            wiki_dir: Directory to store wiki files
            system_prompt_path: Path to system prompt file
        """
        self.gh = Github(token)
        self.repo = self.gh.get_repo(repo)
        self.wiki_dir = Path(wiki_dir)
        self.system_prompt_path = Path(system_prompt_path)
        
        # Ensure directories exist
        self.wiki_dir.mkdir(exist_ok=True, parents=True)
        self.system_prompt_path.parent.mkdir(exist_ok=True, parents=True)
        
        # Ensure we have a system prompt
        self._ensure_system_prompt()
        
        logger.info(f"Initialized WikiManager for repository: {repo}")
    
    def _ensure_system_prompt(self):
        """Create default system prompt if it doesn't exist."""
        if not self.system_prompt_path.exists():
            logger.info(f"Creating default system prompt at {self.system_prompt_path}")
            
            default_prompt = """You are a wiki content creator that writes comprehensive, informative articles on various topics. Your task is to create a well-structured wiki page based on the provided search results.

Follow these guidelines when creating wiki content:

1. Begin with a clear, concise introduction that defines the topic.
2. Structure the content with appropriate headings (using Markdown # syntax).
3. Include relevant facts, history, context, and explanations from the search results.
4. Maintain a neutral, objective tone throughout.
5. Format the content using Markdown for readability.
6. Include internal wiki links in [[double brackets]] when referring to other potentially relevant topics.
7. Be comprehensive but concise - focus on the most important information.
8. If the search results contain conflicting information, acknowledge this and present the different perspectives.
9. End with a brief conclusion summarizing the key points.
10. If appropriate, include a "See Also" section with related topics formatted as [[wiki links]].

Your goal is to create a valuable reference article that would fit well in a knowledge wiki."""
            
            self.system_prompt_path.write_text(default_prompt, encoding="utf-8")
    
    def process_markdown_file(self, file_path: Path) -> List[Dict]:
        """
        Process a markdown file to identify wiki links and create tasks.
        
        Args:
            file_path: Path to markdown file
            
        Returns:
            List of created task issues
        """
        logger.info(f"Processing markdown file: {file_path}")
        
        # Find missing wiki pages
        missing_pages = find_missing_wiki_pages(file_path, self.wiki_dir)
        
        if not missing_pages:
            logger.info("No missing wiki pages found")
            return []
        
        # Create tasks for missing pages
        tasks = []
        for topic in missing_pages:
            task = self._create_wiki_task(topic)
            if task:
                tasks.append(task)
        
        logger.info(f"Created {len(tasks)} tasks for missing wiki pages")
        return tasks
    
    def _create_wiki_task(self, topic: str) -> Dict:
        """
        Create a task for generating a wiki page.
        Uses gh-store conventions to avoid duplicates.
        
        Args:
            topic: Topic to generate content for
            
        Returns:
            Dictionary with task information
        """
        logger.info(f"Creating task for topic: {topic}")
        
        # Check if there's already an open issue for this topic
        labels = ["task", f"UID:{topic}"]
        existing_issues = list(self.repo.get_issues(state="open", labels=labels))
        
        if existing_issues:
            logger.info(f"Task already exists for topic: {topic}")
            return {
                "topic": topic,
                "issue_number": existing_issues[0].number,
                "status": "existing"
            }
        
        # Create task configuration
        task_config = {
            "operator": "generate_wiki",
            "kwargs": {
                "topic": topic,
                "wiki_dir": str(self.wiki_dir),
                "system_prompt_path": str(self.system_prompt_path)
            }
        }
        
        # Create issue
        try:
            issue = self.repo.create_issue(
                title=f"Generate Wiki Page: {topic}",
                body=json.dumps(task_config, indent=2),
                labels=labels
            )
            
            logger.info(f"Created task issue #{issue.number} for {topic}")
            
            return {
                "topic": topic,
                "issue_number": issue.number,
                "status": "created"
            }
        except Exception as e:
            logger.error(f"Failed to create task for {topic}: {str(e)}")
            return None
    
    def check_wiki_page_status(self, topic: str) -> Dict:
        """
        Check if a wiki page exists or is in the process of being generated.
        
        Args:
            topic: Topic to check
            
        Returns:
            Dictionary with status information
        """
        # Check if wiki page exists
        wiki_file = self.wiki_dir / f"{topic}.md"
        if wiki_file.exists():
            return {
                "topic": topic,
                "status": "exists",
                "file_path": str(wiki_file)
            }
        
        # Check if there's an open issue for this topic
        labels = ["task", f"UID:{topic}"]
        existing_issues = list(self.repo.get_issues(state="open", labels=labels))
        
        if existing_issues:
            return {
                "topic": topic,
                "status": "pending",
                "issue_number": existing_issues[0].number
            }
        
        # Check if there's a closed issue for this topic (which means it failed)
        closed_issues = list(self.repo.get_issues(state="closed", labels=labels))
        
        if closed_issues:
            return {
                "topic": topic,
                "status": "failed",
                "issue_number": closed_issues[0].number
            }
        
        return {
            "topic": topic,
            "status": "missing"
        }
    
    def process_changed_files(self, file_paths: List[str]) -> Dict:
        """
        Process a list of changed files to create wiki content tasks.
        
        Args:
            file_paths: List of file paths to process
            
        Returns:
            Summary of processed files and created tasks
        """
        total_files = len(file_paths)
        processed_files = 0
        total_tasks = 0
        
        file_results = {}
        
        for file_path in file_paths:
            path = Path(file_path)
            
            # Skip non-markdown files and files in wiki directory
            if path.suffix.lower() not in ['.md', '.markdown'] or str(path).startswith(str(self.wiki_dir)):
                continue
            
            # Process the file
            if path.exists():
                tasks = self.process_markdown_file(path)
                file_results[file_path] = {
                    "tasks_created": len(tasks),
                    "tasks": tasks
                }
                
                processed_files += 1
                total_tasks += len(tasks)
        
        return {
            "total_files": total_files,
            "processed_files": processed_files,
            "total_tasks": total_tasks,
            "file_results": file_results
        }
