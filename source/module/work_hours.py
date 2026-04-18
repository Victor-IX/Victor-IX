from datetime import datetime
from typing import Optional


def get_work_hours(
    start: datetime,
    end: Optional[datetime],
    hours_per_week: float,
    vacation_days_per_year: float,
) -> str:
    end = end or datetime.now()
    weekdays = _count_weekdays(start, end)
    period_years = (end.date() - start.date()).days / 365.25
    vacation_days = period_years * vacation_days_per_year
    working_days = max(0.0, weekdays - vacation_days)
    hours = working_days * (hours_per_week / 5.0)
    return f"{int(round(hours)):,}"


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
