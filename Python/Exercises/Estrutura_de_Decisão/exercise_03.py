'''
3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
F - Feminino, M - Masculino, Sexo Inválido.
'''

option = input("Digite seu sexo (F - Feminino | M - Masculino): ").upper()
options = {
    "F": "Feminino",
    "M": "Masculino"
    }

try:
    print(options[option])
except KeyError:
    print("Sexo Invalido.")