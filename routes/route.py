from fastapi import APIRouter
from pydantic import BaseModel
from .db import AuthDb



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


@router.get("/login")
async def read_item(username: str = None, password: str = None):
    if username is None and password is None:
        return {False}
    else:
        data = await AuthDb.login_check(username, password)
        return {data}


@router.get("/test")
async def test():
    data = await AuthDb.check_token("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2siOiJvZXhvb2R4c2hzIn0.x8ZEh...")
    print(data)
    if data is None:
        return data
    else:
        print(data)
        return {True}
