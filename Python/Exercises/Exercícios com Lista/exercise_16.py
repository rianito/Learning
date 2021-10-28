'''Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:

    $200 - $299
    $300 - $399
    $400 - $499
    $500 - $599
    $600 - $699
    $700 - $799
    $800 - $899
    $900 - $999
    $1000 em diante 

Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados. '''


lista = [
        [200,0],
        [300,0],
        [400,0],
        [500,0],
        [600,0],
        [700,0],
        [800,0],
        [900,0],
        [1000,0]
        ]

def calcularIntervalo(salario):
    print('foi')
    for i in range(len(lista)):
        if i == len(lista) - 1:
            if salario >= lista[i][0]:
                lista[i][1] += 1
        elif salario >= lista[i][0] and salario < lista[i+1][0]:
            lista[i][1] += 1

while True:
    resposta = input()
    if resposta == 'sair':
        break
    calcularIntervalo(int(resposta))

print(lista)
