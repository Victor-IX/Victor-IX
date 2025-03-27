from github import Github

from config import PAT


def github_user():
    github = Github(PAT)

    rate_limit = github.get_rate_limit()
    core_limit = rate_limit.core.limit
    core_remaining = rate_limit.core.remaining
    core_used = core_limit - core_remaining
    core_reset = rate_limit.core.reset

    print("-------------------------------------")
    print("Requests:")
    print(f"  Limit:     {core_limit}")
    print(f"  Remaining: {core_remaining}")
    print(f"  Used:      {core_used}")
    print(f"  Resets at: {core_reset}")
    print("-------------------------------------")

    user = github.get_user()
    return user


def github_repo(repo: str | None = None):
    user = github_user()
    if not repo:
        return user.get_repos()
    return user.get_repo(repo)
