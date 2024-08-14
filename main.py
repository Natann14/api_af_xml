from SqlServerQueries import NfeQuery
from models import User, Token, TokenData

from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.responses import JSONResponse


from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import timedelta


from typing import Annotated


# uvicorn FastAPI.main:app --host 127.0.0.1 --port 8080 -> alterar porta
# 192.168.101.217
# 45.6.93.66 -> local

app = FastAPI()

# Contexto de encriptação para as senhas
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Dependência OAuth2 (Bearer Token)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "af0c193d49f2fbb2af61d926048503462657f05a1d4904d81d5f0a01abca04b9"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30



@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    obj = NfeQuery()
    user = obj.authenticate_user(form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou Senha Incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = obj.create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}



# Faz a verificação se o usuario esta com o token para acesso aos endpoints
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    obj = NfeQuery()
    obj.autentication_database()
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except: #InvalidTokenError:
        raise credentials_exception
    user = obj.get_user(username=token_data.username)
    #if user is None:
    if not user:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: Annotated[str, Depends(get_current_user)],):
    # if current_user.disabled:
    #     raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[str, Depends(get_current_active_user)],
):
    return JSONResponse(content={"current user": current_user})


# @app.get("/users/me/items/")
# async def read_own_items(
#     current_user: Annotated[User, Depends(get_current_active_user)],
# ):
#     return [{"item_id": "Foo", "owner": current_user.username}]



@app.get("/consultarNfe")
def get_nfe(token: Annotated[str, Depends(get_current_user)]):
    
    obj = NfeQuery()
    obj.autentication_database()
    data = obj.execute_sql_query()

    headers = {"Content-Type": "application/json; charset=utf-8"}
    return JSONResponse(content=data, headers=headers, status_code=200)
