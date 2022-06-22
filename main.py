from fastapi import FastAPI
import fake_data

app = FastAPI()


@app.get("/")
async def Hg():
    return {"asdasd": "Hello World"}


@app.get("/fake")
async def get_fake():
    return fake_data.get_Name()
