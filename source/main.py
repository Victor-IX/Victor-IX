from pathlib import Path

from module.age import daily_readme
from module.archive import get_archived_commit_count
from module.commit import get_total_commits
from module.default_cube import get_removed_cubes
from module.download_count import get_total_download_count
from module.followers import get_github_followers
from module.repo import get_contributed_repo_count, get_user_repo_count
from module.stars import get_total_stars
from module.svg import update_svg

_RESOURCES = Path(__file__).resolve().parent / "resources"


def build_stats() -> dict:
    return {
        "age_data": daily_readme(),
        "commit_data": get_total_commits() + get_archived_commit_count(),
        "star_data": get_total_stars(),
        "repo_data": get_user_repo_count(),
        "contrib_data": get_contributed_repo_count(),
        "follower_data": get_github_followers(),
        "blender_launcher_dl": get_total_download_count(),
        "default_cube": get_removed_cubes(),
    }


def main() -> None:
    stats = build_stats()
    for key, value in stats.items():
        print(f"  {key:<22} {value}")

    for theme in ("dark_mode.svg", "light_mode.svg"):
        update_svg(str(_RESOURCES / theme), stats)


if __name__ == "__main__":
    main()
