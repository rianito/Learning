'''
7. Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

numbers = []

def getMax(numbers):
    max = 0
    for i in range(len(numbers)):
        if numbers[i] > numbers[max]:
            max = i
    return numbers[max]

def getMin(numbers):
    min = 0
    for i in range(len(numbers)):
        if numbers[i] < numbers[min]:
            min = i
    return numbers[min]

for i in range(3):
    while True:
        try:
            numbers.append(float(input(f"Digite o {i+1}o numero: ")))
            break
        except ValueError:
            print("Digite um numero valido.")

print(f"O maior numero foi: {getMax(numbers)}\nO menor foi: {getMin(numbers)}")
