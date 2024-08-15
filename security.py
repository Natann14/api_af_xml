from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from SqlServerQueries import ExecuteQuerie


class UserValidator(ExecuteQuerie):
    
    
    def __init__(self) -> None:
        super().__init__()
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.SECRET_KEY = "af0c193d49f2fbb2af61d926048503462657f05a1d4904d81d5f0a01abca04b9"
        self.ALGORITHM = "HS256"
        self.ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    def get_user(self, username):
        SQL_INSTRUCION = f""" SELECT usuario FROM usuarios WHERE usuario = '{username}' """
        result = self.execute_sql_query_security(SQL_INSTRUCION)
        
        if len(result) == 0:
            return False
        
        user = result[0][0]
        return user

    
    def verify_password(self, password, username):
        SQL_INSTRUCION = f""" SELECT senha FROM usuarios WHERE usuario = '{username}' """
        result = self.execute_sql_query_security(SQL_INSTRUCION)

        if len(result) == 0:
            return False
        
        db_password = result[0][0].replace(" ", "")
        try:
            return self.pwd_context.verify(password, db_password)
        except:
            pass
        
    
    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)    
        return encoded_jwt
    
    
    def authenticate_user(self, username: str, password: str):
        user = self.get_user(username)
        if not user:
            return False
        if not self.verify_password(password, username):
            return False
        return user