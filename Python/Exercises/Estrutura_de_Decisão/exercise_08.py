'''
8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.
'''

prices = []

def getMin(numbers):
    min = 0
    for i in range(len(numbers)):
        if numbers[i] < numbers[min]:
            min = i
    return numbers[min]

for i in range(3):
    while True:
        try:
            prices.append(float(input(f"Digite o preco do {i+1}o produto: ")))
            break
        except ValueError:
            print("Digite um preco valido.")

print(f"O mais barato foi o de: R${getMin(prices)}")