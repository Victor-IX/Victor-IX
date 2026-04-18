from config import REPO_NAME
from module.request_manager import github_repo


def get_total_download_count():
    repo = github_repo(REPO_NAME)
    total_download_count = 0

    for release in repo.get_releases():
        for asset in release.get_assets():
            total_download_count += asset.download_count

    return total_download_count
