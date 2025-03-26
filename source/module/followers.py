if __name__ == "__main__":
    # Get the absolute path of the parent directory
    import os
    import sys

    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

from request_manager import github_user


def get_github_followers() -> int:
    user = github_user()
    return user.followers


if __name__ == "__main__":
    print(get_github_followers())
