
# from Person.person_proto import in_generator
from typing import Any
from faker import Factory


class _AddressProto(Factory):
    def __init__(self,local) -> None:
        self.locality = Factory.create(local)
        super().__init__()

    def create_factory(self):
        return self.locality.city()


if __name__ == "__main__":
    gh = _AddressProto("en_IN")
    print(gh.create_factory())
# for _ in range(10):
#     print(gh.get_address(),end = "\n\n\n")

# fk = Factory.create("en_IN")
# fku = Factory.create("en_US")

# # print(fk.address())
# print(fk.address())
# # print(fk.street_address())
# print(fku.current_country())
