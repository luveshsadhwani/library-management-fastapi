from fastapi import APIRouter
from pydantic import BaseModel
from .db import AuthDb
from fastapi.responses import JSONResponse



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
async def post(authorname, booktitle, subject, publisher, isbn, issued_data):
    index = await AuthDb.count_data()
    entry_data = {
        "id": int(index) + 1,
        "authorname": authorname,
        "booktitle": booktitle,
        "Subject": subject,
        "Publisher": publisher,
        "Isbn": isbn,
        "issued": issued_data
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
    await AuthDb.update_data(index, entry_data)
    return "Done"


@router.post("/deleteentry")
async def delete(entry_id: int):
    data_dict = {
        "id": entry_id
    }
    await AuthDb.delete(data_dict)
    return "Done"


@router.get("/find")
async def find(entry_id: int):
    result = await AuthDb.find_one_entity(entry_id)
    return JSONResponse(content=result)


@router.post("/issued")
async def issued(entry_id: int):
    # Use Regex in the end
    entry_data = {
        "issued": ""
    }
    await AuthDb.set_issue(entry_id, entry_data)
    return "done"


@router.post("/updateissued")
async def update_issue(entry_id: int, data_to_push: str):
    entry_data = {
        "issued": data_to_push
    }
    await AuthDb.set_issue(entry_id, entry_data)
    return "done"


@router.get("/getallissued")
async def get_all_issued():
    result = await AuthDb.get_all_issued()
    return result

"""

    Add another route for saving images in the end

"""
