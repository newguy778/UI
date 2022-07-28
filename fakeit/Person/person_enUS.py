from faker.providers.person import en_US
from typing import Any
from person_proto import _Person


class Person_US(_Person, en_US.Provider):
    temp = []

    def gh(self, quant=1):

        tempa = []

        for i in range(2):
            tempa.append(self.get_cached_val())
        print(tempa)


if __name__ == "__main__":
    temp = []
    for i in range(2):
        gh = Person_US()
        sr = gh.get_cached_val()
        temp.append(sr)
        print(type(sr))
        print(temp)
