from faker.providers.person import en_US
from faker import Factory
from typing import Any
from faker.generator import Generator

in_generator = Factory.create()


class Person_US(en_US.Provider):
    def __init__(self) -> None:
        super().__init__(in_generator)

    def get_first_name(self) -> str:
        return self.first_name()

    def get_last_name(self) -> str:
        return self.last_name()
