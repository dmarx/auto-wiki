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

    # start with prioritized tasks first
    for issue in repo.get_issues(
        state="open", 
        labels=["task","stored-object","prioritized"],
        sort='created',
        direction='asc',
    ):
        labels = [label.name for label in issue.labels]
        if "wontfix" in labels:
            continue
        logger.info(f"[PRIORITY] processing {issue}")
        process_issue(issue.number)

    # after going through all the priority stuff, rebuild the queue
    # this time, we hold out low-priority
    deprioritized=[]
    for issue in repo.get_issues(
        state="open", 
        labels=["task","stored-object"],
        sort='created',
        direction='asc',
    ):
        labels = [label.name for label in issue.labels]
        if ("wontfix" in labels) or ("duplicate" in labels):
            continue
        if "deprioritized" in labels:
            deprioritized.append(issue)
            continue
        logger.info(f"processing {issue}")
        process_issue(issue.number)

    # finally, if we ever make it down this far: process the deprioritized stuff.
    for issue in deprioritized:
        logger.info(f"[LOW PRIORITY] processing {issue}")
        process_issue(issue.number)
    

if __name__ == "__main__":
    get_pending_wiki_tasks()
