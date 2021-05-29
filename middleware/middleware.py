from fastapi import Request
from fastapi.responses import JSONResponse
from .db import AuthDb


async def auth_check(request: Request, call_next):
    if (request.url.path == "/") or (request.url.path == "/docs"):

        response = await call_next(request)
        return response
    else:
        try:

            """
                This Block will be responsible for the authorisation of the api key
            """

            token = request.headers['authorization']
            obj = AuthDb
            trust = await obj.check_token(token)
            if not trust:
                return JSONResponse({"message": "Unauthorized"}, status_code=403)
            else:
                response = await call_next(request)
                return response
        except KeyError:
            return JSONResponse({"message": "Unauthorized"}, status_code=403)
"""
    Middleware works with every route once it has been connected to the main app in main.py
    what this does is that it checks header of the http request
    the line token=request.headers['authorization'] this fetches the auth token from the header
    then the token is sent to the database for verification
    if verified then the endpoints are open to anyone to use otherwise the api returns a 403 and restricts the access

"""
