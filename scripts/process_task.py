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

ddg = DDGS()

with Path("prompts/system_prompt.md").open() as f:
    SYSTEM_PROMPT = f.read()

def with_prompt(
  content: str,
  prompt_path: str|Path|None = None,
  max_len: int=1024,
):
  prompt = ''
  if (not prompt_path) and SYSTEM_PROMPT:
      prompt = SYSTEM_PROMPT
  else:
      with Path(prompt_path).open() as f:
          prompt = f.read()
  if max_len > 0:
    content=content[:(max_len-len(prompt))]
  msg = prompt.format(content=content) # should probably chunk somehow and iterate over chunks
  logger.info(msg)
  response = ddg.chat(msg)
  return response

def wiki_article(
    content: str,
    prompt_path: str|Path|None = None,
    max_len: int=1024,
):
    response = with_prompt(
        content=content,
        prompt_path=prompt_path,
        max_len=max_len,
    )
    logger.info(response)
    result = extract_tag(response, 'content')
    outpath = Path(f"wiki/{content}.md")
    logger.info(f"writing content to {outpath}")
    with outpath.open('w') as f:
        f.write(result)
    return outpath
    
    

# ... should just use locals...
OPERATORS={
    "ddg.chat": ddg.chat,
    "with_prompt": with_prompt,
}

class TaskStatus(Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'

@dataclass
class TaskConfig:
    operator: str
    kwargs: dict
    status: TaskStatus


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
    return result

fire.Fire(main)
