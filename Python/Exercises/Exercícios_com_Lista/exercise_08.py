'''
8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida. 
'''

vetor = []

for i in range(5):
    vetor.append(input(f"Digite a idade da pessoa {i+1}: "))
    vetor.append(input(f"Digite a altura da pessoa {i+1}: "))

for i in range(len(vetor)-1,-1,-1):
    print(vetor[i])