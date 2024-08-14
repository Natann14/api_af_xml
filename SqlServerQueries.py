import pyodbc
# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# from passlib.context import CryptContext

class ExecuteQuerie():

    def __init__(self) -> None:
        self.dados_conexao = (
            "Driver={SQL Server};"
            "Server=localhost;"
            "Database=master;"
            "UID=sa;"
            "PWD=admin123#;"
        )
        

    def execute_sql_query_security(self, sql):

        conexao = pyodbc.connect(self.dados_conexao)
        cursor = conexao.cursor()
        
        SQL_INSTRUCION = f""" {sql} """

        cursor.execute(SQL_INSTRUCION)
        result = cursor.fetchall()
        conexao.close()

        return result
        
        #return dictionary_table
        
    def execute_sql_query_data(self, sql):
        
        conexao = pyodbc.connect(self.dados_conexao)
        cursor = conexao.cursor()

        SQL_INSTRUCION = f""" {sql} """

        cursor.execute(SQL_INSTRUCION)
        result = cursor.fetchall()
        conexao.close()

        table_columns = [column[0] for column in cursor.description]
        dictionary_table = [dict(zip(table_columns, row)) for row in result]
        
        return dictionary_table
    
    
    # def get_user(self, username):
        
    #     conexao = pyodbc.connect(self.dados_conexao)
    #     cursor = conexao.cursor()

    #     SQL_INSTRUCION = f""" SELECT usuario FROM usuarios WHERE usuario = '{username}' """

    #     cursor.execute(SQL_INSTRUCION)
    #     result = cursor.fetchall()
    #     conexao.close()
        
    #     if len(result) == 0:
    #         return False
        
    #     return result[0][0]
    #     #return True

    
    
    # def verify_password(self, password, username):
        
    #     conexao = pyodbc.connect(self.dados_conexao)
    #     cursor = conexao.cursor()

    #     SQL_INSTRUCION = f""" SELECT senha FROM usuarios WHERE usuario = '{username}' """

    #     cursor.execute(SQL_INSTRUCION)
    #     result = cursor.fetchall()
    #     conexao.close()
        
    #     #print('Usuario pesquisado: ', username)
    #     #print('Resultado query:', result[0][0])
        
    #     if len(result) == 0:
    #         return False
        
    #     db_password = result[0][0].replace(" ", "")
        
    #     try:
    #         return self.pwd_context.verify(password, db_password)
    #     except:
    #         pass
        
    
    # def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
    #     to_encode = data.copy()
    #     if expires_delta:
    #         expire = datetime.utcnow() + expires_delta
    #     else:
    #         expire = datetime.utcnow() + timedelta(minutes=15)
    #     to_encode.update({"exp": expire})
    #     encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        
    #     return encoded_jwt
    
    
    # def authenticate_user(self, username: str, password: str):
    #     #obj = NfeQuery()
    #     self.autentication_database()
    #     user = self.get_user(username)
    #     if not user:
    #         return False
    #     if not self.verify_password(password, username):
    #         return False
        
    #     return user
    

    


if __name__ == '__main__':
    obj = ExecuteQuerie()
    # obj.autentication_database()
    # obj.execute_sql_query()
    #obj.get_user('qwe')