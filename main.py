from SqlServerQueries import NfeQuery

from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.responses import JSONResponse


from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import timedelta
from pydantic import BaseModel


# uvicorn FastAPI.main:app --host 127.0.0.1 --port 8080 -> alterar porta
# 192.168.101.217
# 45.6.93.66 -> local

app = FastAPI()

class User(BaseModel):
    #id: int
    username: str


# Definindo o modelo Token para o endpoint POST /token
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str

# Contexto de encriptação para as senhas
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Dependência OAuth2 (Bearer Token)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "af0c193d49f2fbb2af61d926048503462657f05a1d4904d81d5f0a01abca04b9"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)

# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)



# def create_access_token(data: dict, expires_delta: timedelta | None = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt

####################

@app.get("/consultarNfe")
def get_nfe():
    obj = NfeQuery()
    obj.autentication_database()
    data = obj.execute_sql_query()

    headers = {"Content-Type": "application/json; charset=utf-8"}
    return JSONResponse(content=data, headers=headers, status_code=200)




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



async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credential",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = NfeQuery.get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user



@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


