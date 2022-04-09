'''
6. Faça um Programa que leia três números e mostre o maior deles.
'''

numeros = [0,0,0]

for i in numeros:
    numeros[i] = float(input("Digite um numero: "))
maior = 0
for i in numeros:
    if i > maior:
        maior = i

print(f"O maior numero foi o: {maior}")
