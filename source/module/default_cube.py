from datetime import datetime

from config import DATE, CUBES_PER_DAY


def get_removed_cubes() -> str:
    date_format = "%Y-%m-%d"
    date_obj = datetime.strptime(DATE, date_format)
    today = datetime.now()
    delta = today - date_obj
    return str(delta.days * CUBES_PER_DAY)


if __name__ == "__main__":
    print(get_removed_cubes())
