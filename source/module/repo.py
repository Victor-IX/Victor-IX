from config import USER_NAME
from module.archive import get_archived_contrib_count
from module.graphql import run_query
from module.request_manager import github_user


_REPO_COUNT_QUERY = """
query($login: String!, $ownerAffiliation: [RepositoryAffiliation]) {
    user(login: $login) {
        repositories(ownerAffiliations: $ownerAffiliation) {
            totalCount
        }
    }
}
"""


def get_user_repo_count() -> int:
    user = github_user()
    repos = list(user.get_repos())
    return len(repos)


def get_contributed_repo_count() -> int:
    data = run_query(
        _REPO_COUNT_QUERY,
        {"login": USER_NAME, "ownerAffiliation": ["OWNER", "COLLABORATOR", "ORGANIZATION_MEMBER"]},
        "repo.contributed_count",
    )
    live_count = int(data["user"]["repositories"]["totalCount"])
    return live_count + get_archived_contrib_count()
