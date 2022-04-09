'''
23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
'''

numero = float(input("Digite um numero: "))

if numero == int(numero): # round() e math.floor() da na mesma?
    print("Inteiro")
else:
    print("Decimal")

    