from datetime import datetime

DATE = "2014-12-15"


def days_since_date():
    date_format = "%Y-%m-%d"
    date_obj = datetime.strptime(DATE, date_format)
    today = datetime.now()
    delta = today - date_obj
    return delta.days


if __name__ == "__main__":
    print(days_since_date())
