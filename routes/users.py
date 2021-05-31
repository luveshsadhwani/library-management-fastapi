from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    firstName: str


class UpdateUser(BaseModel):
    username: str = None
    password: str = None
    firstName: str = None


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

users = {
    1: {
        "username": "root",
        "password": "root",
        "firstName": "Root"
    },
    2: {
        "username": "root2",
        "password": "root2",
        "firstName": "Rootroot"
    }
}


@router.get("/")
def get_users():
    return users


@router.get("/{userid}")
def get_user(userid: int):
    return users[userid]


@router.post("/create/{userid}")
def create_user(userid: int, user: User): # Request body of parameters based on user model
    if userid in users:
        return {"Error": "User exists"}
    users[userid] = user
    return users[userid]


@router.put("/edit/{userid}", response_model=UpdateUser)
def update_user(userid: int, user: UpdateUser):
    if userid not in users:
        return {"Error": "User does not exist"}
    users[userid] = jsonable_encoder(user)
    return users[userid]


@router.delete("/delete/{userid}")
def delete_user(userid: int):
    if userid not in users:
        return {"Error": "User does not exist"}
    del users[userid]
