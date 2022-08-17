from typing import Any
from faker import Factory


class _AddressProto(Factory):
    def __init__(self, local) -> None:
        self.locality = Factory.create(local)
        super().__init__()

    def get_city(self):
        return self.locality.city()

    def get_state(self):
        return self.locality.state()

    def get_zipcode(self):
        return self.locality.postcode()

    def get_building_number(self):
        return self.locality.building_number()

    def get_street_name(self):
        return self.locality.street_name()

    def get_data(self):
        return {
            "number": self.get_building_number(),
            "street": self.get_street_name(),
            "city": self.get_city(),
            "state": self.get_state(),
            "postal_code": self.get_zipcode(),
        }

    def get_addresses_multiple(self, quantity=1):
        id = 1
        address_data = []
        for i in range(quantity):
            id_counter = {"id": id}
            # addresses = self.get_data()
            id_counter.update(self.get_data())
            address_data.append(id_counter)
            id += 1
        return address_data


if __name__ == "__main__":
    gh = _AddressProto("en_US")
    print(len(gh.get_addresses_multiple(23)))
    # for _ in range(10):
    # gh1 = _AddressProto("en_US")
    # for _ in range(3):
    #     print(gh1.get_addresses_multiple())
    # for _ in range(10):
    #     print(gh.create_factory())
