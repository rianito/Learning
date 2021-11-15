'''Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.'''

def somar(valores):
    soma = 0
    for i in valores:
        soma += i
    return soma

valores = []
for i in range(3):
    valores.append(int(input(f"digite o {i+1}º número: ")))

print(somar(valores))
