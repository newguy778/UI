from faker.providers.person import en_IN
from .person_proto import _Person


class Person_IN(_Person, en_IN.Provider):
    pass


if __name__ == "__main__":
    for i in range(10):
        gh = Person_IN()
        # print(gh.get_first_name())
        # print(gh.get_last_name())
        gh.get_birthdate()
