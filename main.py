from fastapi import FastAPI
from FastAPI.SqlServerQueries import NfeQuery
#from SqlServerQueries import NfeQuery
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel, ValidationError

# uvicorn FastAPI.main:app --host 127.0.0.1 --port 8080 -> alterar porta
# 192.168.101.217
# 45.6.93.66

app = FastAPI()


@app.get("/consultarNfe")
def get_nfe():
    obj = NfeQuery()
    obj.autentication_database()
    data = obj.execute_sql_query()

    headers = {"Content-Type": "application/json; charset=utf-8"}
    return JSONResponse(content=data, headers=headers, status_code=200)


