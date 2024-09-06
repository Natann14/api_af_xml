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
    
    def get_data_nf(self, chave_acesso):
        #SQL_INSTRUCION = f""" SELECT * FROM CONSULTA_NFE """
        SQL_INSTRUCION = f""" SELECT [CODIGO_NOTA]
                                                ,[CODIGO_EMIT]
                                                ,[CODIGO_DEST]
                                                ,[NOTAFISCAL]
                                                ,[URL_ARQUIVO]
                                                ,[UF_EMI_DEST]
                                                ,[VALOR_TOTAL]
                                                ,[ORIGEM]
                                                ,[EMPRESA]
                                                ,[ENVIADO_CONTADOR]
                                                ,[CHAVE_ACESSO]
                                                ,[STATUS]
                                                ,[VERSAO]
                                                ,[STATUSSCHEMA]
                                                ,FORMAT([DATA_EMISSAO], 'dd/MM/yyyy') AS DATA_EMISSAO
                                                ,FORMAT([DATA_ENT_SAIDA], 'dd/MM/yyyy') AS DATA_ENT_SAIDA
                                                ,[BASE_ICMS]
                                                ,[VALOR_ICMS]
                                                ,[BASE_ST]
                                                ,[VALOR_ST]
                                                ,[VALOR_PRODUTOS]
                                                ,[VALOR_FRETE]
                                                ,[VALOR_SEGURO]
                                                ,[VALOR_DESCONTO]
                                                ,[VALOR_II]
                                                ,[VALOR_IPI]
                                                ,[VALOR_PIS]
                                                ,[VALOR_COFINS]
                                                ,[VALOR_OUTROS]
                                                ,[CFOP]
                                                ,[VALIDADO]
                                                ,[BACKUP]
                                                ,[DIRETORIO]
                                                ,[NatOp]
                                                ,FORMAT([DataEntrada], 'dd/MM/yyyy') AS DataEntrada
                                                ,[codigo_transportadora]
                                                ,[sincronizar]
                                                ,[situacao]
                                                ,[contabilizada]
                                                ,[CTe]
                                                ,[CTePossui]
                                                ,[CTeChave_Acesso]
                                                ,[modfrete]
                                                ,[impressa]
                                                ,[ctesituacao]
                                                ,[InfAdcInfCpl]
                                                ,[InfAdcinfAdFisco]
                                                ,[Erro_cadastro_empresa]
                                                ,[InfComplementar]
                                                ,[idDest]
                                                ,[indFinal]
                                                ,[indPres]
                                                ,[ICMSErrado]
                                                ,[tpNF]
                                                ,[iest]
                                                ,[arquivo]
                                                ,[modelo]

                                            FROM [FISCAL_DEFENDER].[dbo].[NFE]
                                            WHERE CHAVE_ACESSO = '{chave_acesso}'
                                            ORDER BY DATA_EMISSAO DESC; """
        
        return self.execute_sql_query_data(SQL_INSTRUCION)