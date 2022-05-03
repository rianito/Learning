'''
13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
se digitar outro valor deve aparecer valor inválido. 
'''

options = [
    "Domingo", "Segunda", "Terca",
    "Quarta", "Quinta", "Sexta",
    "Sabado"
    ]

while True:
    try:
        option = int(input("Digite um numero: "))
        if option > 0 and option < 8:
            print(options[option-1])
        else:
            print("Opcao Invalida")
    except ValueError:
        print("Digite um numero inteiro.")