from fastapi import FastAPI
#from starlette.middleware.base import BaseHTTPMiddleware
from routes import route
#from middleware.middleware import auth_check

app = FastAPI()
# TO RUN THE APP SPECIFY THIS INSTANCE OF THE FastApi class
# uvicorn file_name:instance name --reload

app.include_router(route.router)
# app.add_middleware(BaseHTTPMiddleware, dispatch=auth_check)


"""
  TO run the api in terminal change directory to where main.py is located
  now type uvicorn main:app --reload    where main is the name of the file i.s(main.py in full form ) and app is the instance of the fastapi
  indicated by app = FastApi()
  
  the app will run default on port 8000
  
  to include routes line 10 has been used
  to include middleware line 4 and 2 and 8 has been added but i've commented it to test without the middleware otherwise we will have to send headers with
  each http request

"""
