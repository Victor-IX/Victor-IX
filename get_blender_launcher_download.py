import requests


def get_total_download_count(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases"
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


repo_owner = "victor-ix"
repo_name = "blender-launcher-v2"

total_download_count = get_total_download_count(repo_owner, repo_name)

if total_download_count > 0:
    print(f"The total download count for all releases is: {total_download_count}")
else:
    print("Failed to retrieve the total download count.")
