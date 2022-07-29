from faker.providers.person import en_IN
from person_proto import _Person
from time import perf_counter


class Person_IN(_Person, en_IN.Provider):
    pass


if __name__ == "__main__":
    person_in = Person_IN()
    start = perf_counter()

    print(person_in.get_multiple_person_val(100))
    print(perf_counter() - start)
