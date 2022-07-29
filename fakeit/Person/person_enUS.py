from faker.providers.person import en_US
from typing import Any
from person_proto import _Person


class Person_US(_Person, en_US.Provider):
    pass


if __name__ == "__main__":
    person_instance = Person_US()
    print(person_instance.get_multiple_person_val(2))

    # person_instance.get_multiple_person_val(3)
    # print(person_instance.data_obj)
