from github import Github

from config import PAT, REPO_IGNORE_LIST


def github_user():
    github = Github(PAT)

    try:
        core = github.get_rate_limit().resources.core
        print("-------------------------------------")
        print("Requests:")
        print(f"  Limit:     {core.limit}")
        print(f"  Remaining: {core.remaining}")
        print(f"  Used:      {core.used}")
        print(f"  Resets at: {core.reset}")
        print("-------------------------------------")
    except Exception as e:
        print("-------------------------------------")
        print(f"Rate limit check failed: {e}")
        print("-------------------------------------")

    user = github.get_user()
    return user


def github_repo(repo_name: str | None = None):
    user = github_user()
    if not repo_name:
        repos_list = [repo for repo in user.get_repos() if repo.name not in REPO_IGNORE_LIST]
        return repos_list

    return user.get_repo(repo_name)
