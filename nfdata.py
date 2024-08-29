from api_af_xml.SqlServerQueries import ExecuteSqlServer

class DbData(ExecuteSqlServer):
    
    def __init__(self) -> None:
        super().__init__()
    
    def get_data_nf(self):
        # aqui deve vir a quere da view que vai trazer os xml
        SQL_INSTRUCION = """ SELECT * FROM [ROBOTESTE].[PA000G].[tbl_SubFluxos] """
        return self.execute_sql_query_data(SQL_INSTRUCION)