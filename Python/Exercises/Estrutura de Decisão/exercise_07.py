'''
7. Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

numeros = []

for i in range(3):
    numeros.append(float(input("Digite um numero: ")))

maior = 0
menor = 0
first = True

for i in numeros:
    if first:
        first = False
        maior = i
        menor = i
    else:
        if i > maior:
            maior = i
        elif i < menor:
            menor = i

print(f"O maior numero foi: {maior}\nO menor foi: {menor}")
