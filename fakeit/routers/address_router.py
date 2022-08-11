from fastapi import APIRouter
from fakeit.Address.address_proto import _AddressProto

temp_address = _AddressProto("en_IN")
address_router = APIRouter(prefix="/v1/address")


@address_router.get("/")
def address_home(quantity: int):
    return temp_address.get_addresses_multiple(quantity=quantity)
