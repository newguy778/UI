from fastapi import FastAPI
from person_data import *
import uvicorn

app = FastAPI()


@app.get("/")
async def Hg():
    return {"asdasd": "Hello World"}


@app.get("/fake/firstname")
async def get_fake() -> str:
    return Person_US_API().get_first_name()


@app.get("/fake/lastname")
async def get_fake_lastname() -> str:
    return Person_US_API().get_last_name()

if __name__ == ("__main__"):
    uvicorn.run('routes:app', reload=True, debug=True)
