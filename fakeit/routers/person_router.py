from fastapi import APIRouter
from Person.person_enUS import Person_US
from Person.person_enIN import Person_IN
PERSON_US_INIT = Person_US()

person_router = APIRouter(prefix="/v1/person")


@person_router.get("/")
async def get_us_person(quantity: int = 0):
    qunatity_cache = []
    if not quantity:
        return PERSON_US_INIT.get_full_name()
    for i in range(quantity):
        qunatity_cache.append(PERSON_US_INIT.get_full_name())
    return qunatity_cache


@person_router.get("/{locality}")
async def get_person_local(locality: str):
    if locality == "in":
        return Person_IN().get_full_name()
