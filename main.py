from fastapi import FastAPI
from fastapi import Request, status
from fastapi.responses import JSONResponse

import logging

logging.basicConfig(filename='./logs/api.log', encoding='utf-8', level=logging.DEBUG)

app = FastAPI()

@app.exception_handler(Exception)
async def catch_exception_handler(request: Request, exc: Exception):

    logging.error(exc)

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An error has occurred, please try later"},
    )

@app.get('/check', tags=["Check status"])
def home():
    raise Exception('Vamos a romper el proyecto')
    return {"message": "API it's alive"}

