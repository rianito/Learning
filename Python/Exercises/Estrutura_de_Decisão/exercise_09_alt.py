'''
9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

numbers = []

def getMax(numbers):
    max = 0
    for i in range(len(numbers)):
        if numbers[i] > numbers[max]:
            max = i
    return numbers[max]

def sort(numbers):
    result = []
    while len(numbers) > 0:
        max = getMax(numbers)
        result.append(max)
        numbers.remove(max)
    return result

for i in range(3):
    while True:
        try:
            numbers.append(float(input("Digite um numero: ")))
            break
        except ValueError:
            print("Digite um numero valido.")

print(sort(numbers))