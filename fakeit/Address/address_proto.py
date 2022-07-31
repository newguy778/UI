from faker.providers.address import Provider as AddressProvider
# from Person.person_proto import in_generator
from typing import Any
from faker import Generator,Factory

ty_generator = Generator()

class _AddressProto(AddressProvider):
    def __init__(self) -> None:
        super().__init__(ty_generator)
    
    def get_address(self):
        return self.building_number()
    
    def getek(self):
        return self.city()