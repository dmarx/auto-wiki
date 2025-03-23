# src/wiki_parser.py
"""
Parser for extracting wiki-style links from markdown files.
"""

import re
from pathlib import Path
from typing import Set
from loguru import logger


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


def find_missing_wiki_pages(source_path: Path, wiki_dir: Path) -> set[str]:
    """
    Find wiki links in markdown file that don't have corresponding wiki pages.
    
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
    content = source_path.read_text(encoding="utf-8")
    
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
