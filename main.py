from fastapi import FastAPI
#from starlette.middleware.base import BaseHTTPMiddleware
from routes import route
#from middleware.middleware import auth_check

app = FastAPI()
# TO RUN THE APP SPECIFY THIS INSTANCE OF THE FastApi class
# uvicorn file_name:instance name --reload

app.include_router(route.router)
# app.add_middleware(BaseHTTPMiddleware, dispatch=auth_check)