'''
9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor. 
'''

A = []

for i in range(10):
    A.append(float(input(f"Digite um numero: ")))

resultado = 0.0

for i in A:
    resultado += i*i

print(resultado)