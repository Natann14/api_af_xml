#import pyodbc
import hashlib
# for driver in pyodbc.drivers():
#     print(driver)

# dados_conexao = (
#             "Driver={SQL Server};"
#             "Server=localhost;"
#             "Database=ROBOTESTE;"
#             "UID=sa;"
#             "PWD=Admin1234567#"
#         )


# conexao = pyodbc.connect(dados_conexao)
# cursor = conexao.cursor()

# SQL_INSTRUCION = f""" SELECT * FROM [ROBOTESTE].[CONFIG].[tbl_Credenciais] """

# cursor.execute(SQL_INSTRUCION)
# result = cursor.fetchall()

# print(result)

# conexao.close()

# from passlib.context import CryptContext

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# class Hasher():
#     @staticmethod
#     def verify_password(plain_password, hashed_password):
#         return pwd_context.verify(plain_password, hashed_password)

#     @staticmethod
#     def get_password_hash(password):
#         return pwd_context.hash(password)

# print(Hasher.get_password_hash("admin"))

import requests

# URL do endpoint para obter o token JWT
url = "http://127.0.0.1:8080/token"

# Dados de autenticação (credenciais do usuário)
data = {
    "username": "admin",
    "password": "admin"
}

# Fazendo a requisição para obter o token
response = requests.post(url, data=data)


token = response.json().get("access_token")

url = "http://127.0.0.1:8080/getData"


headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)

print(response.json())

