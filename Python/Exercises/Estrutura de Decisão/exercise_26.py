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

litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustivel (A-alcool | G-gasolina): ")
valor = 0.0

if tipo.upper() == "A":
    valor = litros * 1.9
    if litros > 20:
        valor *= 1.03
    else:
        valor *= 1.05
    print(f"Valor total a pagar: {valor} reais")
elif tipo.upper() == "G":
    valor = litros * 2.5
    if litros > 20:
        valor *= 1.04
    else:
        valor *= 1.06
    print(f"Valor total a pagar: {valor} reais")
else:
    print("Digite um tipo valido!")