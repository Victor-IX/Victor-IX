from datetime import datetime

if __name__ == "__main__":
    # Get the absolute path of the parent directory
    import os
    import sys

    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

from config import DATE, CUBES_PER_DAY


def get_removed_cubes() -> str:
    today = datetime.now()
    delta = today - DATE
    return str(delta.days * CUBES_PER_DAY)


if __name__ == "__main__":
    print(get_removed_cubes())
