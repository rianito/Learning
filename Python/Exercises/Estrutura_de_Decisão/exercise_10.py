'''
10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar 
M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", 
"Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

options = {
    "M": "Bom Dia!",
    "V": "Boa Tarde!",
    "N": "Boa Noite!"
    }

option = input("Digite seu turno: (M - Matutino | V - Vespertino | N - Noturno): ").upper()

try:
    print(options[option])
except KeyError:
    print("Valor Invalido!")