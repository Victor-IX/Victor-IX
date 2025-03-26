from request_manager import github_user


def get_user_repo_count():
    user = github_user()
    repos = list(user.get_repos())
    return len(repos)


if __name__ == "__main__":
    print(get_user_repo_count())
