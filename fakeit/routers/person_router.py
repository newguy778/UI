from datetime import date
from typing import Any
from fastapi import APIRouter, HTTPException
from Person.person_enUS import Person_US
from Person.person_enIN import Person_IN
from Person.person_arabic import Person_arAA

PERSON_US_INIT = Person_US()

person_router = APIRouter(prefix="/v1/person")


@person_router.get("/")
async def get_us_person(quantity: int = 0) -> str:
    if quantity <= 1:
        return PERSON_US_INIT.get_multiple_person_val()

    return PERSON_US_INIT.get_multiple_person_val(quantity)


# @person_router.get("/dob")
# async def gen_date() -> date:
#     return PERSON_US_INIT.get_birthdate()


# @person_router.get("/dict")
# async def get_dict_rsp() -> Any:
#     return PERSON_US_INIT.get_dict()


@person_router.get("/{locality}")
async def get_person_local(locality: str, quantity: int = 1) -> str:
    if locality == "in":
        return Person_IN().get_multiple_person_val(quantity)
    if locality == "ar":
        return Person_arAA().get_multiple_person_val(quantity)

    raise HTTPException(status_code=404, detail="Invalid Locality")


@person_router.get("/*")
async def default_route_not_found():
    return {"status": "Not Foufdggdfgnd"}
