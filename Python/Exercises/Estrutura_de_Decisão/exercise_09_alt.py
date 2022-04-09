'''
9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

numeros = []
ordem = []

for i in range(3):
    numeros.append(float(input("Digite um numero: ")))
    ordem.append(0)

for i in numeros:
    maior = 0
    iguais = 0
    for ii in numeros:
        if i > ii:
            maior += 1
    while ordem[-(maior+1+iguais)] == i:
        iguais += 1
    ordem[-(maior+1+iguais)] = i

print(ordem)