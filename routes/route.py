from fastapi import APIRouter
from pydantic import BaseModel
from .db import AuthDb
import json

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

    return {"data":{str(data)}}
