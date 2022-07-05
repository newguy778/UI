import pytest
import person_data

test_person = person_data.Person_US()


def test_first_name() -> bool:
    type_fname = test_person.get_first_name()
    assert isinstance(type_fname, str)


def test_last_name() -> bool:
    type_lname = test_person.get_last_name()
    assert isinstance(type_lname, str)
