import pyodbc
import cx_Oracle

# dados_conexao = (
#             "Driver={SQL Server};"
#             "Server=(local)"
#             "Database=ROBOTESTE;"
#             "UID=sa;"
#             "PWD=Admin1234567#;"
#             "integrated security=true"
#         )

# dados_conexao = (
#             "Driver={SQL Server};"
#             "Server=SRVCOPER068\SQLEXPRESS;"
#             "Database=FISCAL_DEFENDER;"
#             "UID=sa;"
#             "PWD=Fiscal@2020;"
#         )

dados_conexao = cx_Oracle.connect(
            user='softex',
            password='softex', 
            dsn='192.168.1.46/sesuite2.intranet.copergas.com.br')

# conexao = pyodbc.connect(dados_conexao)
# cursor = conexao.cursor()

# SQL_INSTRUCION = f""" SELECT * FROM CONSULTA_NFE """

# cursor.execute(SQL_INSTRUCION)
# result = cursor.fetchall()
# conexao.close()

cursor = dados_conexao.cursor()
cursor.execute(f""" SELECT TEXTO33 FROM DYNPAG d WHERE texto2 = 'PAG005113' """)

result = cursor.fetchall()
cursor.close()
dados_conexao.close()
print(result)

