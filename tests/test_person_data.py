import pytest
from fakeit.Person.person_proto import _Person
from fakeit.Person.person_enUS import Person_US

person = _Person()

test_person = Person_US()


def test_first_proto() -> bool:
    # type_fname = test_person.get_first_name()
    assert isinstance(person.get_first_name(), str)


def test_last_proto() -> bool:
    # type_lname = test_person.get_last_name()
    assert isinstance(person.get_last_name(), str)


def test_first_US() -> bool:
    # type_fname = test_person.get_first_name()
    assert isinstance(test_person.get_first_name(), str)


def test_last_US() -> bool:
    type_lname = test_person.get_last_name()
    assert isinstance(type_lname, str)


def test_cached_val() -> bool:
    temp_person = _Person()
    assert isinstance(temp_person.cached_val, dict)
