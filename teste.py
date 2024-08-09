# import pyodbc
import json
import requests

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
import pyodbc

# # to get a string like this run:
# # openssl rand -hex 32
# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30


# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
#         "disabled": False,
#     },
#     "alice": {
#         "username": "alice",
#         "full_name": "Alice Chains",
#         "email": "alicechains@example.com",
#         "hashed_password": "$2b$12$gSvqqUPvlXP2tfVFaWK1Be7DlH.PKZbv5H8KnzzVgXXbVxpva.pFm",
#         "disabled": True,
#     },
# }


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     username: str | None = None
#     scopes: list[str] = []


# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disabled: bool | None = None


# class UserInDB(User):
#     hashed_password: str


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_scheme = OAuth2PasswordBearer(
#     tokenUrl="token",
#     scopes={"me": "Read information about the current user.", "items": "Read items."},
# )

############################################################################################################

# dados_conexao = (
#             "Driver={SQL Server};"
#             "Server=SRVCOPER068\SQLEXPRESS;"
#             "Database=FISCAL_DEFENDER;"
#             "UID=sa;"
#             "PWD=Fiscal@2020;"
#         )

# conexao = pyodbc.connect(dados_conexao)
# cursor = conexao.cursor()

# SQL_INSTRUCION = """ SELECT * FROM [FISCAL_DEFENDER].[dbo].[NFE] 
# WHERE CAST(DATA_EMISSAO AS DATE) = DATEADD(DAY, -1, CAST(GETDATE() AS DATE))
# ORDER BY DATA_EMISSAO DESC """

# cursor.execute(SQL_INSTRUCION)

# result = cursor.fetchall()
# conexao.close()

# table_columns = [column[0] for column in cursor.description]
# dictionary_table = [dict(zip(table_columns, row)) for row in result]
# #print(dictionary_table)
# json = json.dumps(dictionary_table, indent=4, default=str).replace("[", "").replace("]", "")
# print(json)


# x = requests.get('http://127.0.0.1:8080/consultarNfe')
# data = x.json()
# for dado in data:
#     print(dado['CODIGO_NOTA'])
#     #print(type(dado['CODIGO_NOTA']))

# dados_conexao = (
#             "Driver={SQL Server};"
#             "Server=SRVCOPER068\SQLEXPRESS;"
#             "Database=FISCAL_DEFENDER;"
#             "UID=sa;"
#             "PWD=Fiscal@2020;"
#         )

# conexao = pyodbc.connect(dados_conexao)
# cursor = conexao.cursor()

# SQL_INSTRUCION = """ SELECT * FROM CONSULTA_NFE """

# cursor.execute(SQL_INSTRUCION)

# result = cursor.fetchall()
# conexao.close()

# #print(result)

# table_columns = [column[0] for column in cursor.description]
# dictionary_table = [dict(zip(table_columns, row)) for row in result]

# print(dictionary_table[0])