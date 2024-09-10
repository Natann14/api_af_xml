from api_af_xml.security import UserValidator
from api_af_xml.nfdata import DbData
from api_af_xml.models import User, Token, TokenData
from api_af_xml.validate_af import AfValidation
from api_af_xml.sesuitePAG import SeSuiteQuery
from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from datetime import timedelta
from typing import Annotated


app = FastAPI()

# Dependência OAuth2 (Bearer Token)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# Dependencia validacao de usuario no banco de dados
validator = UserValidator()
# Dependencia da classe que faz a query dos dados no banco
get_data = DbData()
# Dependencia da classe para associação verificar qual af esta relacionada ao xml
af_relacionada = AfValidation()
# Dependencia da classe para associação PAG x af
pag_relacionado = SeSuiteQuery()

# Faz a verificação se o usuario esta com o token para acesso aos endpoints
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, validator.SECRET_KEY, algorithms=[validator.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except:
        raise credentials_exception
    user = validator.get_user(username=token_data.username)
    #if user is None:
    if not user:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: Annotated[str, Depends(get_current_user)],):
    # if current_user.disabled:
    #     raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


# @app.get("/users/me/", response_model=User)
# async def read_users_me(
#     current_user: Annotated[str, Depends(get_current_active_user)],
# ):
#     return JSONResponse(content={"current user": current_user})


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = validator.authenticate_user(form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou Senha Incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=validator.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = validator.create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/", include_in_schema=False)
def redirect():
    return RedirectResponse(url="/docs")


@app.get("/AfAssociadaPAG")
def af_associada_pag(token: Annotated[str, Depends(get_current_user)], num_PAG):
    data = pag_relacionado.find_pag_associated(num_PAG)
    return JSONResponse(content=data, status_code=200)


@app.get("/ChaveAcessoAssociadaAf")
def chave_associada_af(token: Annotated[str, Depends(get_current_user)], num_AF):
    data = af_relacionada.find_associated_access_key(num_AF)
    return JSONResponse(content=data, status_code=200)


@app.get("/AfAssociadaChaveAcesso")
def af_associada_chave(token: Annotated[str, Depends(get_current_user)], chave_acesso):
    data = af_relacionada.find_associated_aff(chave_acesso)
    return JSONResponse(content=data, status_code=200)


@app.get("/DadosNFE")
def get_nfe(token: Annotated[str, Depends(get_current_user)], chave_acesso):
    data = get_data.get_data_nf(chave_acesso)
    headers = {"Content-Type": "application/json; charset=utf-8"}
    return JSONResponse(content=data, headers=headers, status_code=200)
