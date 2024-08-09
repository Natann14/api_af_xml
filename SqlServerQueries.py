import pyodbc

class NfeQuery():

    def __init__(self) -> None:
        self.dados_conexao = None

    def autentication_database(self):

        self.dados_conexao = (
            "Driver={SQL Server};"
            "Server=SRVCOPER068\SQLEXPRESS;"
            "Database=FISCAL_DEFENDER;"
            "UID=sa;"
            "PWD=Fiscal@2020;"
        )

    def execute_sql_query(self):

        conexao = pyodbc.connect(self.dados_conexao)
        cursor = conexao.cursor()

        SQL_INSTRUCION = """ SELECT * FROM CONSULTA_NFE """

        cursor.execute(SQL_INSTRUCION)
        result = cursor.fetchall()
        conexao.close()

        table_columns = [column[0] for column in cursor.description]
        dictionary_table = [dict(zip(table_columns, row)) for row in result]
        
        return dictionary_table
    

    


if __name__ == '__main__':
    obj = NfeQuery()
    obj.autentication_database()
    obj.execute_sql_query()