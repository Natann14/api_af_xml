import pyodbc

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