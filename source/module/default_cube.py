from datetime import datetime

from config import DATE, CUBES_PER_DAY


def days_since_date() -> str:
    date_format = "%Y-%m-%d"
    date_obj = datetime.strptime(DATE, date_format)
    today = datetime.now()
    delta = today - date_obj
    return str(delta.days * CUBES_PER_DAY)


if __name__ == "__main__":
    print(days_since_date())
