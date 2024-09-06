from api_af_xml.oraclequeries import OracleQuery
import cx_Oracle

class AfValidation(OracleQuery):

    def __init__(self) -> None:
        super().__init__()
    
    def find_associated_aff(self, chave_acesso):

        self.conexao = cx_Oracle.connect(
            user='SILASSOUZA',
            password='abc123',
            dsn='192.168.0.241/TESTE.intranet.copergas.com.br')

        SQL_INSTRUCION = f""" SELECT pc.NUMPEDC from ENTRADA e
                                inner join
                                ITEM_ENTRADA ie on e.ENTRADA = ie.ENTRADA and e.FILIAL = ie.FILIAL
                                inner join
                                ITENS_PED_COMPRA ipc on ie.ITEM_PEDIDO = ipc.ITEM and ie.NUMPEDC = ipc.NUMPEDC and ie.FILIAL = ipc.FILIAL
                                inner join
                                PEDIDO_COMPRA pc on ie.NUMPEDC = pc.NUMPEDC and ie.FILIAL = pc.FILIAL
                                WHERE
                                e.COD_CHAVE_ACESSO_NFEL = '{chave_acesso}' """
        
        return self.execute_oracle_query(SQL_INSTRUCION)
    

    def find_associated_access_key(self, num_AF):

        self.conexao = cx_Oracle.connect(
            user='SILASSOUZA',
            password='abc123',
            dsn='192.168.0.241/TESTE.intranet.copergas.com.br')

        SQL_INSTRUCION = f""" SELECT e.COD_CHAVE_ACESSO_NFEL from ENTRADA e
                    inner join
                    ITEM_ENTRADA ie on e.ENTRADA = ie.ENTRADA and e.FILIAL = ie.FILIAL
                    inner join
                    ITENS_PED_COMPRA ipc on ie.ITEM_PEDIDO = ipc.ITEM and ie.NUMPEDC = ipc.NUMPEDC and ie.FILIAL = ipc.FILIAL
                    inner join 
                    PEDIDO_COMPRA pc on ie.NUMPEDC = pc.NUMPEDC and ie.FILIAL = pc.FILIAL
                    WHERE
                    ie.NUMPEDC = '{num_AF}' """
        
        return self.execute_oracle_query(SQL_INSTRUCION)