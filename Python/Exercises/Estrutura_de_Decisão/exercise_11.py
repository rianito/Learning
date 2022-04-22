'''
11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe 
contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o 
seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

import os

reajuste = {
    1500: 5,
    700: 10,
    280: 15,
    0: 20
    }

def clearConsole():
    tipo = os.name
    if tipo == "nt":
        os.system("cls")
        return True
    elif tipo == "posix":
        os.system("clear")
        return True
    else:
        print("Nao foi possivel identificar seu sistema operacional.")
        exit()

def showResult(salary, percent):
    print(f'''
{'='*52}
{'Salario Anterior:':<32} {salary:<16} R$
{'Percentual de Aumento:':<32} {percent:<16} %
{'Valor do Aumento:':<32} {salary * percent/100:<16} R$
{'Salario Atual:':<32} {salary + salary * percent/100:<16} R$
{'='*52}
''')

clearConsole()

while True:
    try:
        salary = float(input("Digite o salario: R$"))
        for i in reajuste.keys():
            if salary > i:
                showResult(salary, reajuste[i])
                break
        break
    except ValueError:
        print("Digite um numero valido.")