from datetime import datetime, timezone

from github import Github

from config import PAT, REPO_IGNORE_LIST


def _format_reset_in(reset_at: datetime) -> str:
    if reset_at.tzinfo is None:
        reset_at = reset_at.replace(tzinfo=timezone.utc)
    seconds = max(int((reset_at - datetime.now(timezone.utc)).total_seconds()), 0)
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours}h {minutes}m {secs}s"


def print_rate_limit() -> None:
    github = Github(PAT)
    try:
        core = github.get_rate_limit().resources.core
        print("-------------------------------------")
        print("Requests:")
        print(f"  Limit:     {core.limit}")
        print(f"  Remaining: {core.remaining}")
        print(f"  Used:      {core.used}")
        print(f"  Reset in:  {_format_reset_in(core.reset)}")
        print("-------------------------------------")
    except Exception as e:
        print("-------------------------------------")
        print(f"Rate limit check failed: {e}")
        print("-------------------------------------")


def github_user():
    github = Github(PAT)
    user = github.get_user()
    return user


def github_repo(repo_name: str | None = None):
    user = github_user()
    if not repo_name:
        repos_list = [repo for repo in user.get_repos() if repo.name not in REPO_IGNORE_LIST]
        return repos_list

    return user.get_repo(repo_name)
