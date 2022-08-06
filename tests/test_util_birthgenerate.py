import pytest

from fakeit.Person.person_util.birthdate_generator import (
    random_month,
    random_day,
    random_year,
)


def test_month():
    get_month = next(random_month())
    assert 1 <= get_month <= 12


def test_days():
    thirty1 = random_day(1)
    assert 1 <= thirty1 <= 31

    thirty = random_day(4)
    assert 1 <= thirty <= 30

    feb = random_day(2)
    assert 1 <= feb <= 29
