'''
1. Faça um Programa que peça dois números e imprima o maior deles.
'''

numbers = []

for i in range(2):
    while True:
        try:
            numbers.append(float(input(f"Digite o {i+1}o numero: ")))
            break
        except ValueError:
            print("Digite um numero valido.")

max = numbers[0] if numbers[0] > numbers[1] else numbers[1]
print(f"O maior numero foi o: {max}")