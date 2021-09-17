'''
6. Faça um Programa que leia três números e mostre o maior deles.
'''

numeros = []

for i in range(3):
    numeros.append(float(input("Digite um numero: ")))

maior = 0.0

for i in numeros:
    maior = numeros[0]
    if i > maior:
        maior = i

print(f"O maior numero foi o: {maior}")