from faker.providers.address import Provider as AddressProvider
# from Person.person_proto import in_generator
from typing import Any
from faker import Generator,Factory,Faker

class _AddressProto:

    def __init__(self,local) -> None:
        self.locality = Faker(local)
    
    
    def get_address(self):
        return self.locality.current_country()
        

gh = _AddressProto('jp_JP')

print(gh.get_address())