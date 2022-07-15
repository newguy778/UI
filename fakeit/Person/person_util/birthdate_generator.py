import datetime
import random
DAYS_IN_MONTH = list(range(1, 32))

"""
TODO: Generate Date based on locality format create function and call that instead.

"""


def random_month() -> int:
    yield random.choice(list(range(1, 13)))


def random_day(month) -> int:
    thrity1_days: set = {1, 3, 5, 7, 8, 10, 12}
    thirty_days: set = {4, 6, 9, 11}
    feb: int = 2
    if month in thrity1_days:
        return random.choice(DAYS_IN_MONTH)
    if month in thirty_days:
        return random.choice(DAYS_IN_MONTH[:30])
    if month == feb:
        return random.choice(DAYS_IN_MONTH[:29])


def random_year() -> int:
    datetime.MINYEAR: int = 1945
    CURRENT_YEAR: int = datetime.date.today().year
    yield random.choice(list(range(datetime.MINYEAR, CURRENT_YEAR-19)))


def _generate_date() -> tuple:
    year, month = next(random_year()), next(random_month())
    return year, month, random_day(month)


def generate_date_obj() -> datetime.date:
    return datetime.date(*_generate_date())


if __name__ == "__main__":
    for _ in range(12):
        print(generate_date_obj())
