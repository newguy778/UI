from fastapi import APIRouter
from Person.person_enUS import Person_US
from Person.person_enIN import Person_IN


person_router = APIRouter(prefix="/v1/person")


@person_router.get("/")
async def get_us_person():
    return Person_US().get_full_name()


@person_router.get("/{locality}")
async def get_person_local(locality: str):
    if locality == "in":
        return Person_IN().get_full_name()
