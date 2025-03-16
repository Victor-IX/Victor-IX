if __name__ == "__main__":
    # Get the absolute path of the parent directory
    import os
    import sys

    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

from config import USER_NAME, HEADERS
from request_manager import request_get


def calculate_total_stars():
    """Fetch all repositories for a given user, handling pagination."""
    repos = []
    page = 1

    while True:
        # GitHub API URL for user repositories
        url = f"https://api.github.com/users/{USER_NAME}/repos?per_page=100&page={page}"

        response = request_get(url, headers=HEADERS)
        page_repos = response.json()

        if not page_repos:
            break

        repos.extend(page_repos)
        page += 1

    stars = sum(repo["stargazers_count"] for repo in repos)
    return stars


if __name__ == "__main__":
    print(calculate_total_stars())
