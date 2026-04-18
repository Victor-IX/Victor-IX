from module.request_manager import github_repo


def get_total_stars():
    stars = 0
    repos = github_repo()
    for repo in repos:
        stars += repo.stargazers_count

    return stars
