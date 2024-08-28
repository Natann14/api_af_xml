from api_af_xml.SqlServerQueries import ExecuteQuerie

class DbData(ExecuteQuerie):
    
    def __init__(self) -> None:
        super().__init__()
    
    def get_data_nf(self):
        
        SQL_INSTRUCION = """ SELECT * FROM [ROBOTESTE].[PA000G].[tbl_SubFluxos] """
        return self.execute_sql_query_data(SQL_INSTRUCION)