from module.request_manager import github_user


def get_github_followers() -> int:
    user = github_user()
    return user.followers
