# scripts/process_task.py
import ast
from dataclasses import dataclass
from enum import Enum
#import json
from pathlib import Path

from duckduckgo_search import DDGS
import fire
#from gh_store.core.access import AccessControl
from loguru import logger

from gh_store.cli.commands import get_store
from gh_store.core.exceptions import AccessDeniedError

from create_wiki_tasks import process_file as queue_new_links
from llamero.utils import commit_and_push


ddg = DDGS()

with Path("prompts/system_prompt.md").open() as f:
    SYSTEM_PROMPT = f.read()

def with_prompt(
  content: str,
  prompt_path: str|Path|None = None,
  max_len: int=2048,
):
  prompt = ''
  if (not prompt_path) and SYSTEM_PROMPT:
      prompt = SYSTEM_PROMPT
  else:
      with Path(prompt_path).open() as f:
          prompt = f.read()
  if max_len > 0:
    content=content[:(max_len-len(prompt))]
  logger.info(f"content: {content}")
  msg = prompt.format(content=content) # should probably chunk somehow and iterate over chunks
  logger.info(msg)
  response = ddg.chat(msg)
  return response

def wiki_article(
    content: str,
    prompt_path: str|Path|None = None,
    max_len: int=2048,
    force: bool|None = False
):
    outpath = Path(f"wiki/{content}.md")
    if outpath.exists() and (not force):
        logger.info(f"{outdir} already exists. set `force=True` to overwrite.")
        return
        
    response = with_prompt(
        content=content,
        prompt_path=prompt_path,
        max_len=max_len,
    )
    logger.info(response)
    result = extract_tag(response, 'content')
    
    logger.info(f"writing content to {outpath}")
    with outpath.open('w') as f:
        f.write(result)
    queue_new_links(outpath)
    commit_and_push(outpath)
    return outpath
    
    

# ... should just use locals...
OPERATORS={
    "ddg.chat": ddg.chat,
    "with_prompt": with_prompt,
    "wiki_article": wiki_article,
}

class TaskStatus(Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'

@dataclass
class TaskConfig:
    operator: str
    kwargs: dict
    status: TaskStatus
    force: bool|None = False


def extract_tag(text: str, tag: str = 'content'):
    start = f"<{tag}>"
    end = f"</{tag}>"
    if start not in text:
        return None
    _,text = text.split(start, 1)
    if end in text:
        text,_ = text.split(end, 1)
    return text


def main(issue_number):
    store = get_store()
    issue = store.repo.get_issue(issue_number)
    # if not store.access_control.validate_issue_creator(issue):
    #     raise AccessDeniedError(
    #             "Tasks can only be processed for issues created by "
    #             "repository owner or authorized CODEOWNERS"
    #         )
    logger.info(issue)
    data = ast.literal_eval(issue.body)
    logger.info(data)
    config = TaskConfig(**data)
    logger.info(config)
    
    op = OPERATORS[config.operator]
    result = op(**config.kwargs)
    logger.info(result)
    issue.edit(state='closed')
    return result

if __name__ == '__main__':
    fire.Fire(main)
