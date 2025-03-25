# scripts/process_wiki_tasks.py
"""
Process wiki tasks from gh-store and generate content.
"""

from loguru import logger
from process_task import main as process_issue

import os
import shutil
import time
from github import Github


# min seconds between requests
CADENCE=45


LAST_REQUEST=time.time()-CADENCE

def handle_wait():
    global LAST_REQUEST
    now = time.time()
    delta = now - LAST_REQUEST
    wait = CADENCE-delta
    if wait > 0:
        logger.info(f"pausing for {int(wait)} sec to maintain a request cadence of {CADENCE} sec")
        time.sleep(wait)
    LAST_REQUEST = time.time()

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
        handle_wait()

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
        handle_wait()

    # finally, if we ever make it down this far: process the deprioritized stuff.
    for issue in deprioritized:
        logger.info(f"[LOW PRIORITY] processing {issue}")
        process_issue(issue.number)
        handle_wait()
    

if __name__ == "__main__":
    get_pending_wiki_tasks()
