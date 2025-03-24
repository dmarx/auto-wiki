# scripts/process_task.py
import ast
from dataclasses import dataclass
import json
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
  target: str|Path,
  prompt: str=SYSTEM_PROMPT,
  max_len: int=1024,
):
  with Path(target).open() as f:
    content = f.read()
  if max_len > 0:
    content=content[:(max_len-len(prompt))]
  msg = prompt.format(content=content) # should probably chunk somehow and iterate over chunks
  logger.info(msg)
  response = ddg.chat(msg)
  return response
  

# ... should just use locals...
OPERATORS={
    "ddg.chat": ddg.chat,
    "with_prompt": with_prompt,
}

@dataclass
class TaskConfig:
    operator: str
    kwargs: dict


#def main(config: dict):
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
