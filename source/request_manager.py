from github import Github

from config import PAT


def github_user():
    github = Github(PAT)
    user = github.get_user()
    return user


def github_repo(repo: str | None = None):
    user = github_user()
    if not repo:
        return user.get_repos()
    return user.get_repo(repo)
