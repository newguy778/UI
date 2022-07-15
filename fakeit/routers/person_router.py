from datetime import date
from typing import Any
from fastapi import APIRouter
from Person.person_enUS import Person_US
from Person.person_enIN import Person_IN
import json
PERSON_US_INIT = Person_US()

person_router = APIRouter(prefix="/v1/person")


@person_router.get("/")
async def get_us_person(quantity: int = 0) -> str:
    qunatity_cache = []
    if quantity <= 1:
        return PERSON_US_INIT.get_full_name()
    return PERSON_US_INIT.get_quantity_full_name(quantity)


@person_router.get("/dob")
async def gen_date() -> date:
    return PERSON_US_INIT.get_birthdate()


@person_router.get("/dict")
async def get_dict_rsp() -> Any:
    return PERSON_US_INIT.get_dict()


@person_router.get("/{locality}")
async def get_person_local(locality: str) -> str:
    if locality == "in":
        return Person_IN().get_full_name()
