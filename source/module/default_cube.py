from datetime import datetime

from config import DATE, CUBES_PER_DAY


def get_removed_cubes() -> str:
    today = datetime.now()
    delta = today - DATE
    return str(delta.days * CUBES_PER_DAY)
