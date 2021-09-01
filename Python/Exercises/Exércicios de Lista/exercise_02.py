'''
2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''

lista = []

for i in range(10):
    lista.append(input("Digite um numero: "))

for i in range(len(lista)-1,-1,-1):
    print(lista[i])
