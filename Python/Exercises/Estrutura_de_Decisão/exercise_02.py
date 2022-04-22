'''
2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''

while True:
    try:
        number = float(input("Digite um numero: "))
        message = "O numero e positivo" if number > 0 else "O numero e negativo"
        print(message)
        break
    except ValueError:
        print("Digite um numero valido.")