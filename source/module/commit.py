if __name__ == "__main__":
    # Get the absolute path of the parent directory
    import os
    import sys

    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

from request_manager import github_repo
from config import USER_NAME


def get_total_stars():
    commits_count = 0
    repos = github_repo()
    for repo in repos:
        commits = repo.get_commits(author=USER_NAME)
        commits_count += commits.totalCount

    return commits_count


if __name__ == "__main__":
    print(get_total_stars())
