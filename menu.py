from Fatura import Fatura
dictproduto = [
]
while True:
    nomeproduto = input("Nome do Produto: ")
    quantidade = int(input(f"Quantidade de itens do produto{nomeproduto}: "))
    valorUnitario = float(input("Valor da unidade do produto: "))
    single = {}
    single["nomeproduto"] = nomeproduto
    single["quantidade"] = quantidade
    single["valorUnitario"] = valorUnitario
    dictproduto.append(single)
    ask = input("Digite / para gerar fatura, ou pressione Enter para adicionar mais itens: \n")
    if ask == "/":
        break
fatura_roger = Fatura(dictproduto)
print(fatura_roger)