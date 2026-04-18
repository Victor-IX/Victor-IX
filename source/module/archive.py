import json
from pathlib import Path

_ARCHIVE_PATH = Path(__file__).resolve().parent.parent / "cache" / "repository_archive.json"


def _load() -> list[dict]:
    if not _ARCHIVE_PATH.exists():
        return []
    with _ARCHIVE_PATH.open("r", encoding="utf-8") as f:
        return json.load(f).get("repositories", [])


def get_archived_commit_count() -> int:
    return sum(int(repo.get("my_commits", 0)) for repo in _load())


def get_archived_contrib_count() -> int:
    return len(_load())
