import pyodbc

# dados_conexao = (
#             "Driver={SQL Server};"
#             "Server=(local)"
#             "Database=ROBOTESTE;"
#             "UID=sa;"
#             "PWD=Admin1234567#;"
#             "integrated security=true"
#         )

dados_conexao = (
            "Driver={SQL Server};"
            "Server=SRVCOPER068\SQLEXPRESS;"
            "Database=FISCAL_DEFENDER;"
            "UID=sa;"
            "PWD=Fiscal@2020;"
        )


conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

SQL_INSTRUCION = f""" SELECT * FROM CONSULTA_NFE """

cursor.execute(SQL_INSTRUCION)
result = cursor.fetchall()
conexao.close()