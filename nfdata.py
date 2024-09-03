from api_af_xml.SqlServerQueries import ExecuteSqlServer

class DbData(ExecuteSqlServer):
    
    def __init__(self) -> None:
        super().__init__()
        self.dados_conexao = (
            "Driver={SQL Server};"
            "Server=SRVCOPER068\SQLEXPRESS;"
            "Database=FISCAL_DEFENDER;"
            "UID=sa;"
            "PWD=Fiscal@2020;"
        )
    
    def get_data_nf(self):
        # aqui deve vir a query da view que vai trazer os xml
        #SQL_INSTRUCION = """ SELECT * FROM [ROBOTESTE].[PA000G].[tbl_SubFluxos] """
        SQL_INSTRUCION = """ SELECT * FROM CONSULTA_NFE """
        return self.execute_sql_query_data(SQL_INSTRUCION)