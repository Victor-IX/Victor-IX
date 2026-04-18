from datetime import datetime

from config import MAYA_CRASH_DATE, MAYA_CRASHES_PER_DAY


def get_maya_crashes() -> str:
    today = datetime.now()
    return str(_count_weekdays(MAYA_CRASH_DATE, today) * MAYA_CRASHES_PER_DAY)


def _count_weekdays(start: datetime, end: datetime) -> int:
    days = (end.date() - start.date()).days
    if days <= 0:
        return 0
    full_weeks, remainder = divmod(days, 7)
    count = full_weeks * 5
    start_weekday = start.weekday()
    for i in range(remainder):
        if (start_weekday + i) % 7 < 5:
            count += 1
    return count
