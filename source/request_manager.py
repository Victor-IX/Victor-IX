from github import Github

from config import PAT, REPO_IGNORE_LIST


def github_user():
    github = Github(PAT)

    try:
        rate_limit = github.get_rate_limit()
        if hasattr(rate_limit, "core"):
            core = rate_limit.core
            core_limit = core.limit
            core_remaining = core.remaining
            core_used = core_limit - core_remaining
            core_reset = core.reset
        else:
            core_limit = getattr(rate_limit, "limit", 5000)
            core_remaining = getattr(rate_limit, "remaining", "Unknown")
            core_used = core_limit - core_remaining if isinstance(core_remaining, int) else "Unknown"
            core_reset = getattr(rate_limit, "reset", "Unknown")

        print("-------------------------------------")
        print("Requests:")
        print(f"  Limit:     {core_limit}")
        print(f"  Remaining: {core_remaining}")
        print(f"  Used:      {core_used}")
        print(f"  Resets at: {core_reset}")
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
