import pytest
from Person.person_enUS import Person_US

test_person = Person_US()


def test_first_name() -> bool:
    type_fname = test_person.get_first_name()
    assert isinstance(type_fname, str)


def test_last_name() -> bool:
    type_lname = test_person.get_last_name()
    assert isinstance(type_lname, str)
