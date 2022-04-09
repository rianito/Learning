'''
13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
se digitar outro valor deve aparecer valor inválido. 
'''

dias = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terca-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sabado"
}

numero = float(input("Digite um numero inteiro: "))

if numero > 0 and numero <= len(dias):
    print(dias[numero])
else:
    print("Valor invalido")