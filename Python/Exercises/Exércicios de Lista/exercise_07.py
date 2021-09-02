'''
7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, 
a multiplicação e os números.
'''

numeros = []

for i in range(5):
    numeros.append(int(input("Digite um numero inteiro: ")))

for i in range(2):
    resultado = numeros[0]
    for ii in range(1,len(numeros)):
        if i == 0:
            resultado += numeros[ii]
        else: 
            resultado *= numeros[ii]
    print(resultado)
print(numeros)
