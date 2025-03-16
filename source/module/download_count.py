import requests

from config import REPO


def get_total_download_count():
    url = f"{REPO}/releases"
    params = {"per_page": 100}
    total_download_count = 0

    while True:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            releases = response.json()

            for release in releases:
                for asset in release["assets"]:
                    total_download_count += asset["download_count"]

            if "next" in response.links:
                url = response.links["next"]["url"]
                params = {}
            else:
                break
        else:
            break

    return total_download_count


if __name__ == "__main__":
    print(get_total_download_count())
