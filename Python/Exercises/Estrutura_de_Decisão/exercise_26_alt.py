'''
26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de 
combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente 
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

# while True:
#     dados = {
#         "quantidade_litros": "(em litros)",
#         "tipo_combustivel": "(A - alcool | G - Gasolina)"
#         }

#     for i in dados:
#         dados[i] = input(f"Digite o/a {i} {dados[i]}: ")

#     if dados["tipo_combustivel"].upper() == "A":
#         dados["tipo_combustivel"] = float(dados["quantidade_litros"]) * 1.9
#     elif dados["tipo_combustivel"].upper() == "B":
#         dados["tipo_combustivel"] = float(dados["quantidade_litros"]) * 2.5
#     else:
#         print("Digite um tipo valido!")
#         break
    
#     print("foi")