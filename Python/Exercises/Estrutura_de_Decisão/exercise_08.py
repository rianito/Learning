'''
8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.
'''

precos = []

for i in range(3):
    precos.append(float(input("Digite o preco: ")))

menor = 0
first = True
for i in precos:
    if first:
        first = False
        menor = i
    else:
        if i < menor:
            menor = i
print(f"O mais barato foi o de: R${menor}")