if __name__ == "__main__":
    # Get the absolute path of the parent directory
    import os
    import sys

    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)


from config import REPO_NAME
from request_manager import github_repo


def get_total_download_count():
    repo = github_repo(REPO_NAME)
    total_download_count = 0

    for release in repo.get_releases():
        for asset in release.get_assets():
            total_download_count += asset.download_count

    return total_download_count


if __name__ == "__main__":
    print(get_total_download_count())
