from faker.providers.person import en_US
from typing import Any
from person_proto import _Person


class Person_US(_Person, en_US.Provider):
    pass


if __name__ == "__main__":
    gh = Person_US()
    print(gh.get_full_name())
    print(gh.get_birthdate())
