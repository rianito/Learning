'''
28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara 
o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o 
tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações 
da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor 
a pagar.
'''
tipos = {
    "FILE DUPLO": [4.9, 5.8],
    "ALCATRA": [5.9, 6,8],
    "PICANHA": [6.9, 7.8]
    }
tipo = input("Tipo da carne: ").upper()
quantidade = float(input("Quantidade de carne: "))
pagamento = input("Forma de pagamento: ")
valor = 0

if quantidade > 5:
    valor = quantidade * tipos[tipo][1]
else:
    valor = quantidade * tipos[tipo][0]

if pagamento.upper() == "CARTAO TABAJARA":
    print(f"TIPO: {tipo}\nQUANTIDADE: {quantidade}\nPRECO TOTAL: {valor}\nFORMA DE PAGAMENTO: {pagamento}\nVALOR DESCONTO: {valor * 0.05}\n VALOR A PAGAR: {valor}")
else:
    print(f"TIPO: {tipo}\nQUANTIDADE: {quantidade}\nPRECO TOTAL: {valor}\nFORMA DE PAGAMENTO: {pagamento}\nVALOR DESCONTO: 0\n VALOR A PAGAR: {valor}")







