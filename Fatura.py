from datetime import datetime
class Fatura():
    def __init__ (self, nome_valor:list):
        valor_total = 0
        for i in range (len(nome_valor)):
            self.nome = nome_valor[i]["nomeproduto"]
            self.valor = nome_valor[i]["valorUnitario"]
            self.quantidade = nome_valor[i]["quantidade"]
            valor_total += nome_valor[i]["valorUnitario"] * nome_valor[i]["quantidade"]
        data = datetime.now()
        formatted_data = data.strftime("%d/%m/%Y")
        formatted_time = data.strftime("%H:%M:%S")
        print(f'''

                                 FATURA

              
LOJA:Tech V1RUZ        ENDEREÇO:Rua da Misericórdia, Nº 156, Salvador, BA         
--------------------------------------------------------------------------
TEL.: +55 71 9 9266-6666
DATA:{formatted_data}                          TIME:{formatted_time}
--------------------------------------------------------------------------'''
)
        for i in range (len(nome_valor)):
            print(f"{nome_valor[i]['nomeproduto']}  x[{nome_valor[i]['quantidade']}]                      {nome_valor[i]['valorUnitario']}")
        print(f'''
--------------------------------------------------------------------------
TOTAL:                                                        {round(valor_total,2)}
--------------------------------------------------------------------------
                                 OBRIGADO
''')