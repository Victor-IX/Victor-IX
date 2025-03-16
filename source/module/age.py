import datetime
from dateutil import relativedelta

from config import BIRTHDATE


def daily_readme():
    diff = relativedelta.relativedelta(datetime.datetime.today(), BIRTHDATE)
    years = f"{diff.years} year{format_plural(diff.years)}"
    months = f"{diff.months} month{format_plural(diff.months)}"
    days = f"{diff.days} day{format_plural(diff.days)}"
    birthday = " 🎂" if (diff.months == 0 and diff.days == 0) else ""

    return f"{years}, {months}, {days}{birthday}"


def format_plural(unit):
    return "s" if unit != 1 else ""


if __name__ == "__main__":
    print(daily_readme())
