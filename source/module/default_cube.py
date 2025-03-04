from datetime import datetime

# Date when starting using blender, year, month, day
DATE = datetime.datetime(2014, 12, 15)
# Estimated number of default cubes removed per day
CUBES_PER_DAY: int = 1


def days_since_date() -> str:
    date_format = "%Y-%m-%d"
    date_obj = datetime.strptime(DATE, date_format)
    today = datetime.now()
    delta = today - date_obj
    return str(delta.days * CUBES_PER_DAY)


if __name__ == "__main__":
    print(days_since_date())
