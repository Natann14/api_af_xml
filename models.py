from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str

# Modelo Token para o endpoint POST /token
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str
    
        
# class UserInDB(User):
#     hashed_password: str