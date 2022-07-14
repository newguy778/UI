
from typing import Any, Dict

from faker import Factory, Generator
from faker.providers.person import Provider as PersonProvider
from utils_pro.birthdate_generator import generate_date


class _Person(PersonProvider):

    cached_val: Dict[str, str] = {}

    def __init__(self) -> None:
        super().__init__(Factory.create())

    def is_empty(self, *args):
        for i in args:
            if i not in self.cached_val:
                return True
        return False

    def get_first_name(self) -> str:
        self.cached_val['first_name'] = self.first_name()
        return self.cached_val['first_name']

    def get_last_name(self) -> str:
        self.cached_val['last_name'] = self.last_name()
        return self.cached_val['last_name']

    def get_full_name(self) -> tuple:
        if self.is_empty('first_name', 'last_name'):
            return ",".join((self.get_first_name(), self.get_last_name()))
        self.get_first_name(), self.get_last_name()
        full_name = (
            self.cached_val["first_name"], self.cached_val["last_name"])
        return ",".join(full_name)

    def get_quantity_full_name(self, quantity: int):
        pass

    def get_birthdate(self) -> tuple:
        return generate_date()
