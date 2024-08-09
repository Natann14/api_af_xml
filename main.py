from fastapi import FastAPI, status, Depends, HTTPException
from FastAPI.SqlServerQueries import NfeQuery
from fastapi.responses import JSONResponse
#import models
#from database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session


# uvicorn FastAPI.main:app --host 127.0.0.1 --port 8080 -> alterar porta
# 192.168.101.217
# 45.6.93.66 -> local

app = FastAPI()


@app.get("/consultarNfe")
def get_nfe():
    obj = NfeQuery()
    obj.autentication_database()
    data = obj.execute_sql_query()

    headers = {"Content-Type": "application/json; charset=utf-8"}
    return JSONResponse(content=data, headers=headers, status_code=200)


