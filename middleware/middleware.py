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
            trust = await obj.check_token("sdikjansjafirdask")
            if not trust:
                return JSONResponse({"message": "Unauthorized"}, status_code=403)
            else:
                response = await call_next(request)
                return response
        except KeyError:
            return JSONResponse({"message": "Unauthorized"}, status_code=403)

"""
HAB CON TO DB
"""