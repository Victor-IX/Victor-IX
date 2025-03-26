if __name__ == "__main__":
    # Get the absolute path of the parent directory
    import os
    import sys

    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

from config import USER_NAME
from request_manager import request_get


def get_github_followers() -> int:
    url = f"https://api.github.com/users/{USER_NAME}"

    user_data = request_get(url, headers={"User-Agent": "GitHub-Follower-Counter"}).json()
    return user_data.get("followers", 0)


if __name__ == "__main__":
    print(get_github_followers())
