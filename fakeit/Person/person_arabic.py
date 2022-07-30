from faker.providers.person import ar_AA
from person_proto import _Person


class Person_arAA(_Person, ar_AA.Provider):
    pass


if __name__ == "__main__":
    gh = Person_arAA()
    gh.get_cached_val()
    print(gh.cached_val)
