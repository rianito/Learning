'''
9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

numeros = []

for i in range(3):
    numeros.append(float(input("Digite um numero: ")))

numeros.sort()
numeros.reverse()
print(numeros)