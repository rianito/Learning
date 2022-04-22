'''
6. Faça um Programa que leia três números e mostre o maior deles.
'''

numbers = []

def getMax(numbers):
    max = 0
    for i in range(len(numbers)):
        if numbers[i] > numbers[max]:
            max = i
    return numbers[max]

for i in range(3):
    while True:
        try:
            numbers.append(float(input(f"Digite o {i+1}o numero: ")))
            break
        except ValueError:
            print("Digite um numero valido.")

print(f"O maior numero foi o: {getMax(numbers)}")