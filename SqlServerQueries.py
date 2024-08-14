import pyodbc
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

class NfeQuery():

    def __init__(self) -> None:
        self.dados_conexao = None
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.SECRET_KEY = "af0c193d49f2fbb2af61d926048503462657f05a1d4904d81d5f0a01abca04b9"
        self.ALGORITHM = "HS256"
        self.ACCESS_TOKEN_EXPIRE_MINUTES = 30

    def autentication_database(self):

        self.dados_conexao = (
            "Driver={SQL Server};"
            "Server=localhost;"
            "Database=master;"
            "UID=sa;"
            "PWD=admin123#;"
        )

    def execute_sql_query(self):

        conexao = pyodbc.connect(self.dados_conexao)
        cursor = conexao.cursor()

        SQL_INSTRUCION = """ SELECT id, nome, CONVERT(varchar(50), preco) AS preco_formatado, quantidade FROM produtos """

        cursor.execute(SQL_INSTRUCION)
        result = cursor.fetchall()
        conexao.close()

        table_columns = [column[0] for column in cursor.description]
        dictionary_table = [dict(zip(table_columns, row)) for row in result]
        
        return dictionary_table
    
    
    def get_user(self, username):
        
        conexao = pyodbc.connect(self.dados_conexao)
        cursor = conexao.cursor()

        SQL_INSTRUCION = f""" SELECT * FROM usuarios WHERE usuario = '{username}' """

        cursor.execute(SQL_INSTRUCION)
        result = cursor.fetchall()
        conexao.close()
        
        if len(result) == 0:
            return False
        
        return True

    
    
    def verify_password(self, password, username):
        
        conexao = pyodbc.connect(self.dados_conexao)
        cursor = conexao.cursor()

        SQL_INSTRUCION = f""" SELECT senha FROM usuarios WHERE usuario = '{username}' """

        cursor.execute(SQL_INSTRUCION)
        result = cursor.fetchall()
        conexao.close()
        
        #print('Usuario pesquisado: ', username)
        #print('Resultado query:', result[0][0])
        
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
        #obj = NfeQuery()
        self.autentication_database()
        user = self.get_user(username)
        if not user:
            return False
        if not self.verify_password(password, username):
            return False
        print('Usuariooooooo: ', user)
        return user
    

    


if __name__ == '__main__':
    obj = NfeQuery()
    obj.autentication_database()
    # obj.execute_sql_query()
    #obj.get_user('qwe')