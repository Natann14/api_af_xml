#import cx_Oracle


class OracleQuery():

    def __init__(self) -> None:
        self.conexao = None
    

    def execute_oracle_query(self, query):
        
        cursor = self.conexao.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        table_columns = [column[0] for column in cursor.description]
        dictionary_table = [dict(zip(table_columns, row)) for row in result]

        cursor.close()
        self.conexao.close()
        
        return dictionary_table