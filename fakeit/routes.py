from fastapi import FastAPI
from Person.person_enUS import Person_US
from Person.person_enIN import Person_IN
from routers import person_router
from end_points import API
import uvicorn

app = FastAPI()
app.include_router(person_router.person_router)


@app.get("/")
async def Hg():
    return {"asdasd": "Hello World"}


# @app.get("/v1/firstname")
# async def get_fake() -> str:
#     return US_API_GEN.get_first_name()


# @app.get(API.lastname)
# async def get_fake_lastname() -> str:
#     return US_API_GEN.get_last_name()


# @app.get("/v1/in/lastname")
# async def get_fake_lastname() -> str:
#     return IN_API_GEN.get_last_name()



if __name__ == ("__main__"):
    uvicorn.run('routes:app',reload=True, debug=True, host='0.0.0.0',port=8000)
