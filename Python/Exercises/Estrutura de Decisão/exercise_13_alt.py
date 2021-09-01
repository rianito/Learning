'''
13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
se digitar outro valor deve aparecer valor inválido. 
'''

numero = float(input("Digite um numero: "))

if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda-feira")
elif numero == 3:
    print("Terca-feira")
elif numero == 4:
    print("Quarta-feira") 
elif numero == 5:
    print("Quinta-feira")
elif numero == 6:
    print("Sexta-feira")
elif numero == 7:
    print("Sabado")
else:
    print("Valor invalido")