if __name__ == "__main__":
    # Get the absolute path of the parent directory
    import os
    import sys

    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)


from config import REPO
from request_manager import request_get


def get_total_download_count():
    url = f"{REPO}/releases"
    params = {"per_page": 100}
    total_download_count = 0

    while True:
        response = request_get(url, params=params)
        releases = response.json()

        for release in releases:
            for asset in release["assets"]:
                total_download_count += asset["download_count"]

        if "next" in response.links:
            url = response.links["next"]["url"]
            params = {}
        else:
            break

    return total_download_count


if __name__ == "__main__":
    print(get_total_download_count())
