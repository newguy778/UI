from fastapi import FastAPI
from Person.person_data import *
import uvicorn

app = FastAPI()
US_API_GEN = Person_US_API()


@app.get("/")
async def Hg():
    return {"asdasd": "Hello World"}


@app.get("/fake/firstname")
async def get_fake() -> str:
    return US_API_GEN.get_first_name()


@app.get("/fake/lastname")
async def get_fake_lastname() -> str:
    return US_API_GEN.get_last_name()

if __name__ == ("__main__"):
    uvicorn.run('routes:app', reload=True, debug=True)
