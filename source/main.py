import argparse
from pathlib import Path

from config import (
    METRIC_EMPIRE_END,
    METRIC_EMPIRE_HOURS_PER_WEEK,
    METRIC_EMPIRE_START,
    METRIC_EMPIRE_VACATION_DAYS_PER_YEAR,
    NVIZZIO_END,
    NVIZZIO_HOURS_PER_WEEK,
    NVIZZIO_START,
    NVIZZIO_VACATION_DAYS_PER_YEAR,
    STAR_CITIZEN_END,
    STAR_CITIZEN_HOURS_PER_WEEK,
    STAR_CITIZEN_START,
    STAR_CITIZEN_VACATION_DAYS_PER_YEAR,
)
from module.age import daily_readme
from module.archive import get_archived_commit_count
from module.commit import get_total_commits
from module.default_cube import get_removed_cubes
from module.download_count import get_total_download_count
from module.followers import get_github_followers
from module.maya_crash import get_maya_crashes
from module.repo import get_contributed_repo_count, get_user_repo_count
from module.request_manager import print_rate_limit
from module.stars import get_total_stars
from module.svg import update_svg
from module.work_hours import get_work_hours

_RESOURCES = Path(__file__).resolve().parent / "resources"


_STEPS = (
    ("age_data", "Calculating age", daily_readme),
    ("commit_data", "Fetching commit count", lambda: get_total_commits() + get_archived_commit_count()),
    ("star_data", "Fetching star count", get_total_stars),
    ("repo_data", "Fetching owned repo count", get_user_repo_count),
    ("contrib_data", "Fetching contributed repo count", get_contributed_repo_count),
    ("follower_data", "Fetching follower count", get_github_followers),
    ("blender_launcher_dl", "Fetching Blender Launcher downloads", get_total_download_count),
    ("default_cube", "Fetching removed default cubes", get_removed_cubes),
    ("maya_crashes", "Counting Maya crashes encountered", get_maya_crashes),
    (
        "nvizzio_hours",
        "Calculating hours at Nvizzio",
        lambda: get_work_hours(
            NVIZZIO_START,
            NVIZZIO_END,
            NVIZZIO_HOURS_PER_WEEK,
            NVIZZIO_VACATION_DAYS_PER_YEAR,
        ),
    ),
    (
        "metric_empire_hours",
        "Calculating hours at Metric Empire",
        lambda: get_work_hours(
            METRIC_EMPIRE_START,
            METRIC_EMPIRE_END,
            METRIC_EMPIRE_HOURS_PER_WEEK,
            METRIC_EMPIRE_VACATION_DAYS_PER_YEAR,
        ),
    ),
    (
        "star_citizen_hours",
        "Calculating hours on Star Citizen",
        lambda: get_work_hours(
            STAR_CITIZEN_START,
            STAR_CITIZEN_END,
            STAR_CITIZEN_HOURS_PER_WEEK,
            STAR_CITIZEN_VACATION_DAYS_PER_YEAR,
        ),
    ),
)


def build_stats() -> dict:
    stats = {}
    total = len(_STEPS)
    for index, (key, label, func) in enumerate(_STEPS, start=1):
        print(f"[{index}/{total}] {label}...")
        stats[key] = func()
    return stats


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--request",
        action="store_true",
        help="Show GitHub API rate limit info and exit",
    )
    args = parser.parse_args()

    if args.request:
        print_rate_limit()
        return

    print("=== Collecting stats ===")
    stats = build_stats()

    print("\n=== Results ===")
    for key, value in stats.items():
        print(f"  {key:<22} {value}")

    print("\n=== Updating SVG files ===")
    themes = ("dark_mode.svg", "light_mode.svg")
    for index, theme in enumerate(themes, start=1):
        print(f"[{index}/{len(themes)}] Writing {theme}...")
        update_svg(str(_RESOURCES / theme), stats)

    print("\nDone.")


if __name__ == "__main__":
    main()
