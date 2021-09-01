'''
6. Faça um Programa que leia três números e mostre o maior deles.
'''

numeros = []

for i in range(3):
    numeros.append(float(input("Digite um numero: ")))

maior = 0
first = True

for i in numeros:
    if first:
        first = False
        maior = i
    else:
        if i > maior:
            maior = i

print(f"O maior numero foi o: {maior}")
