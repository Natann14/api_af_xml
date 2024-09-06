import pyodbc

class ExecuteSqlServer():

    def __init__(self) -> None:
        self.dados_conexao = None
        

    def execute_sql_query_security(self, sql):
        conexao = pyodbc.connect(self.dados_conexao)
        cursor = conexao.cursor()

        cursor.execute(sql)
        result = cursor.fetchall()
        conexao.close()
        return result
        
    def execute_sql_query_data(self, sql):
        conexao = pyodbc.connect(self.dados_conexao)
        cursor = conexao.cursor()
        
        cursor.execute(sql)
        result = cursor.fetchall()
        conexao.close()

        table_columns = [column[0] for column in cursor.description]
        dictionary_table = [dict(zip(table_columns, row)) for row in result]
        return dictionary_table