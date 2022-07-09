from fastapi import FastAPI
from Person.person_data import *
from Person.person_enIN import Person_IN

import uvicorn

app = FastAPI()
US_API_GEN = Person_US()
IN_API_GEN = Person_IN()


@app.get("/")
async def Hg():
    return {"asdasd": "Hello World"}


@app.get("/v1/firstname")
async def get_fake() -> str:
    return US_API_GEN.get_first_name()


@app.get("/v1/lastname")
async def get_fake_lastname() -> str:
    return US_API_GEN.get_last_name()


@app.get("/v1/in/lastname")
async def get_fake_lastname() -> str:
    return IN_API_GEN.get_last_name()


@app.get("/v1/dob")
async def get_fake_lastname() -> str:
    return IN_API_GEN.get_birthdate()

if __name__ == ("__main__"):
    uvicorn.run('routes:app', reload=True, debug=True)
