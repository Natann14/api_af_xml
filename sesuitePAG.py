from api_af_xml.oraclequeries import OracleQuery
import cx_Oracle

class SeSuiteQuery(OracleQuery):

    def __init__(self) -> None:
        super().__init__()

    
    def find_pag_associated(self, pag):

        self.conexao = cx_Oracle.connect(
            user='softex',
            password='softex',
            dsn='192.168.1.46/sesuite2.intranet.copergas.com.br')
        
        SQL_INSTRUCION = f""" SELECT AF.TEXTO1 AS NUM_AF
                FROM DYNGRIDAF af LEFT JOIN DYNPAG d ON af.OIDFKPAGGRIDAF1 = d.OID 
                WHERE d.TEXTO2 = '{pag}' """
        
        return self.execute_oracle_query(SQL_INSTRUCION)