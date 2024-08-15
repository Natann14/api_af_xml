from SqlServerQueries import ExecuteQuerie

class DbData(ExecuteQuerie):
    
    def __init__(self) -> None:
        super().__init__()
    
    def get_data_nf(self):
        
        SQL_INSTRUCION = """ SELECT id, nome, CONVERT(varchar(50), preco) AS preco_formatado, quantidade FROM produtos """
        return self.execute_sql_query_data(SQL_INSTRUCION)