from faker import Generator, Factory
from faker.providers.person import Provider as PersonProvider
from typing import Any


class Person(PersonProvider):
    def __init__(self) -> None:
        super().__init__(Factory.create())
