from faker.providers.address import en_IN
from address_proto import _AddressProto, ty_generator

class Address_IN(_AddressProto,en_IN.Provider):
    pass


gh = Address_IN()

print (gh.get_address())
print (gh.getek())
