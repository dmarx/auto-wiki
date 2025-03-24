from github import Github

g = Github(os.environ["GITHUB_TOKEN"])
repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
response = repo.get_label("fake label")
print(response)
