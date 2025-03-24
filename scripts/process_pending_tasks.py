# scripts/process_wiki_tasks.py
"""
Process wiki tasks from gh-store and generate content.
"""

# import json
# import os
# import subprocess
# from pathlib import Path
# from typing import Dict, Any, List
# from datetime import datetime, timezone

#import fire
from loguru import logger
#from gh_store.core.store import GitHubStore

from process_task import main as process_issue

import os
import shutil
from github import Github



def get_pending_wiki_tasks():
    g = Github(os.environ["GITHUB_TOKEN"])
    repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])

    pending=[]
    for issue in repo.get_issues(state="open", labels=["task","stored-object"]):
        labels = [label.name for label in issue.labels]
        if "wontfix" in labels:
            continue
        pending.append(issue)
    logger.info(f"pending issues: {pending}")
    return pending

if __name__ == "__main__":
    get_pending_wiki_tasks()
