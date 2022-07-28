
from typing import Any, Dict, List

from faker import Factory, Generator
from faker.providers.person import Provider as PersonProvider
from person_util.birthdate_generator import generate_date_obj
from datetime import date
in_generator = Generator()


class _Person(PersonProvider):

    cached_val: Dict[Any, Any] = {}
    data_obj: Dict[str, List] = {'data': []}
    arr_data = []
    counter = 0

    quantity_val_fullname: set = set()

    def __init__(self) -> None:
        super().__init__(in_generator)

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
        self.cached_val["full_name"] = ",".join(
            (self.cached_val['last_name'], self.cached_val['first_name']))
        return self.cached_val['full_name']

    def get_birthdate(self) -> date:
        return generate_date_obj()

    def get_cached_val(self):
        self.get_first_name()
        self.get_last_name()
        self.get_full_name()
        self.counter += 1
        return self.cached_val

    def get_quantity_full_name(self, quantity: int):
        self.arr_data.clear()
        for i in range(quantity):
            self.arr_data.append(self.cached_val)
        return self.arr_data
