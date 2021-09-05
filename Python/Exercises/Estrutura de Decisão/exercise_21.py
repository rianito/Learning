'''
21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a 
valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas 
disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo 
de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na 
máquina.
a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, 
uma nota de 50, uma nota de 5 e uma nota de 1;
b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

valor = 0
notas = [0,0,0,0,0] # 100,50,10,5,1
while True:
    valor = int(input("Digite o valor do saque: "))
    if valor >= 10 and valor <= 600:
        break
    else:
        print("Apenas valores entre 10 e 600 reais.")

while valor > 0:
    if valor >= 100:
        valor -= 100
        notas[0] += 1
    elif valor >= 50:
        valor -= 50
        notas[1] += 1
    elif valor >= 10:
        valor -= 10
        notas[2] += 1
    elif valor >= 5:
        valor -= 5
        notas[3] += 1
    else:
        notas[4] = valor
        valor = 0

print(notas)