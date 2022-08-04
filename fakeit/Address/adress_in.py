# from faker.providers.address import en_I
from address_proto import _AddressProto

class Address_IN(_AddressProto):
    def __init__(self) -> None:
        super().__init__('en_IN')
    pass


gh = Address_IN()

print(gh.create_factory())