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
        return info


@router.post("/entry")
async def post(authorname, booktitle, subject, publisher, isbn, issued_data):
    result = await AuthDb.get_last_inserted_item()
    index = result[0]['id']
    entry_data = {
        "id": int(index) + 1,
        "authorname": authorname,
        "booktitle": booktitle,
        "Subject": subject,
        "Publisher": publisher,
        "Isbn": isbn,
        "issued": issued_data,
        "issued_date": "",
        "return_date": ""
    }
    await AuthDb.post_data(entry_data)
    return "Done"


# Test it out if fine don't change
@router.post("/updateentry")
async def update(id, authorname, booktitle, subject, publisher, isbn):
    entry_data = {
        "authorname": authorname,
        "booktitle": booktitle,
        "Subject": subject,
        "Publisher": publisher,
        "Isbn": isbn
    }
    await AuthDb.update_data(id, entry_data)
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


# This needs changing
@router.post("/issued")
async def issued(entry_id: int):
    # Use Regex in the end
    entry_data = {
        "issued": "",
        "issued_date": "",
        "return_date": ""
    }
    await AuthDb.set_issue(entry_id, entry_data)
    return "done"


# This needs changing
@router.post("/updateissued")
async def update_issue(entry_id: int, data_to_push: str, date_of_issue: str, return_date: str):
    entry_data = {
        "issued": data_to_push,
        "issued_date": date_of_issue,
        "return_date": return_date
    }
    await AuthDb.set_issue(entry_id, entry_data)
    return "done"


@router.get("/getallissued")
async def get_all_issued():
    result = await AuthDb.get_all_issued()
    return result


@router.get("/employee_info")
async def employee_num(employee_id: str):
    result = await AuthDb.single_employee_data(employee_id)
    return result


@router.get("/deleted_account")
async def check_deleted_acc(employee_id: str):
    result = await AuthDb.check_deleted_employee(employee_id)

    return result


@router.post("/update_employee_info")
async def update(employee_id: str, firstname, lastname, email, phone, designation):
    entry_data = {
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "phone": phone,
        "designation": designation
    }
    await AuthDb.update_single_employee_data(employee_id, entry_data)
    return "Done"


@router.get("/filter_search")
async def filter_search(field: str, val: str):
    info = await AuthDb.filtered_data(field, val)
    return info


@router.get("/filter_issued")
async def filter_issued(field, val):
    info = await AuthDb.filtered_data_issued(field, val)
    return info

"""
    Add User
    Update User
    Delete User
    Login using Data
    Add another route for saving images in the end

"""
