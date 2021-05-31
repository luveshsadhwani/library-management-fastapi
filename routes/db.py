from fastapi import APIRouter
from pydantic import BaseModel
from .db import AuthDb

# from fastapi.responses import UJSONResponse


router = APIRouter()


class Data(BaseModel):
    Authorization: str


@router.get("/")
async def home():
    await AuthDb.do_insert()
    return "HELLO WORLD"


@router.get("/data")
async def data():
    info = await AuthDb.return_data()
    return info


@router.get("/login")
async def read_item(username: str = None, password: str = None):
    if username is None and password is None:
        return {False}
    else:
        info = await AuthDb.login_check(username, password)
        return {info}


@router.post("/entry")
async def post(authorname, booktitle, subject, publisher, isbn):
    index = await AuthDb.count_data()
    entry_data = {
        "id": int(index) + 1,
        "authorname": authorname,
        "booktitle": booktitle,
        "Subject": subject,
        "Publisher": publisher,
        "Isbn": isbn
    }
    await AuthDb.post_data(entry_data)
    return "Done"


@router.post("/updateentry")
async def update(index, authorname, booktitle, subject, publisher, isbn):
    entry_data = {
        "authorname": authorname,
        "booktitle": booktitle,
        "Subject": subject,
        "Publisher": publisher,
        "Isbn": isbn
    }
    x = await AuthDb.update_data(index, entry_data)
    return "Done"


@router.post("/deleteentry")
async def delete(entry_id: int):
    data_dict = {
        "id": entry_id
    }
    await AuthDb.delete(data_dict)
    return "Done"


@router.get("/findone")
async def find(entry_id: int):
    result = await AuthDb.find_one_entity(entry_id)
    return result

"""

    Add another route for saving images in the end

"""
