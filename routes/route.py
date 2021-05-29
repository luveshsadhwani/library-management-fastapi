from fastapi import APIRouter
from pydantic import BaseModel
from .db import AuthDb
#from fastapi.responses import UJSONResponse


router = APIRouter()


class Data(BaseModel):
    Authorization: str


@router.get("/")
async def home():
    await AuthDb.do_insert()
    return "HELLO WORLD"


@router.get("/data")
async def data():
    data = await AuthDb.return_data()
    return [{"data": data}]

""" TEST FOR CHECKING TOKEN DONT WANT THE WHOLE WORLD TO ACCESS OUR API """
@router.get("/test")
async def test():
    data = await AuthDb.check_token("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2siOiJvZXhvb2R4c2hzIn0.x8ZEh...")
    print(data)
    if data is None:
        return data
    else:
        print(data)
        return {True}

    """ 5 ROUTES """
