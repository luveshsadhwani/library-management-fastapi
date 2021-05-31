from fastapi import FastAPI
# from starlette.middleware.base import BaseHTTPMiddleware
from routes import route
from fastapi.middleware.cors import CORSMiddleware
# from middleware.middleware import auth_check

app = FastAPI()
# TO RUN THE APP SPECIFY THIS INSTANCE OF THE FastApi class
# uvicorn file_name:instance name --reload

app.include_router(route.router)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://localhost:8080/data",
    "http://localhost:3000/home/dashboard"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_middleware(BaseHTTPMiddleware, dispatch=auth_check)
