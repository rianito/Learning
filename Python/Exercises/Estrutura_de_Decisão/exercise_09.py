'''
9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

numbers = []

for i in range(3):
    while True:
        try:
            numbers.append(float(input("Digite um numero: ")))
            break
        except ValueError:
            print("Digite um numero valido.")

numbers.sort()
numbers.reverse()
print(numbers)