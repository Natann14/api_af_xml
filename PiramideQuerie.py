#import cx_Oracle
import pyodbc


class AssociateDocs():

    def __init__(self) -> None:
        # self.conexao = cx_Oracle.connect(
        #     user='PIRAMIDE', 
        #     password='PIRAMIDE', 
        #     dsn='192.168.0.241/TESTE.intranet.copergas.com.br')
        self.conexao = (
            "Driver={SQL Server};"
            "Server=SRVCOPER068\SQLEXPRESS;"
            "Database=FISCAL_DEFENDER;"
            "UID=sa;"
            "PWD=Fiscal@2020;"
        )
        
    
    def find_af(self, chave_acesso):

        with self.conexao as conection:
            with conection.cursor() as cursor:
                cursor.execute(f""" SELECT * from ENTRADA e 
                                inner join
                                ITEM_ENTRADA ie on e.ENTRADA = ie.ENTRADA and e.FILIAL = ie.FILIAL
                                inner join
                                ITENS_PED_COMPRA ipc on ie.ITEM_PEDIDO = ipc.ITEM and ie.NUMPEDC = ipc.NUMPEDC and ie.FILIAL = ipc.FILIAL
                                inner join 
                                PEDIDO_COMPRA pc on ie.NUMPEDC = pc.NUMPEDC and ie.FILIAL = pc.FILIAL
                                WHERE
                                e.COD_CHAVE_ACESSO_NFEL = '{chave_acesso}'  """)
                
        result = cursor.fetchall()
    
    
    def link_xml_af(self):
        
        with self.conexao as conection:
            with conection.cursor() as cursor:
                cursor.execute(f"""  """)
