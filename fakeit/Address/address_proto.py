from faker.providers.address import Provider as AddressProvider

# from Person.person_proto import in_generator
from typing import Any
from faker import Generator, Factory, Faker


class _AddressProto:
    def __init__(self, local) -> None:
        self.locality = Faker(local)

    def get_address(self):
        return self.locality.address()


gh = _AddressProto("en_IN")

print(gh.get_address())

# fk = Factory.create("en_IN")
# fku = Factory.create("en_US")

# # print(fk.address())
# print(fk.address())
# # print(fk.street_address())
# print(fku.current_country())
