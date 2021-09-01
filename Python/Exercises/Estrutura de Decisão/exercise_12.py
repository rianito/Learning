'''
12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do 
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto 
menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas 
no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

valor_Hora = float(input("Valor da hora: R$"))
horas_Trabalhadas = float(input("Horas trabalhadas: "))

salario_Bruto = horas_Trabalhadas * valor_Hora
desconto = 0

if salario_Bruto > 0 and salario_Bruto <= 900:
    desconto = 0
elif salario_Bruto > 900 and salario_Bruto <= 1500:
    desconto = 5
elif salario_Bruto > 1500 and salario_Bruto <= 2500:
    desconto = 15
elif salario_Bruto > 2500:
    desconto = 20

print(f'''
Salario Bruto ({horas_Trabalhadas} * {valor_Hora})         : R${salario_Bruto}
(-) IR ({desconto}%)                         : R${salario_Bruto * (desconto/100)}
(-) Sindicato (3%)                   : R${salario_Bruto * 0.03}
FGTS (11%)                           : R${salario_Bruto * 0.11}
Total de descontos                   : R${(salario_Bruto * (desconto/100)) + salario_Bruto * 0.03}
Salario liquido                      : R${salario_Bruto - (salario_Bruto * 0.03 + (salario_Bruto * (desconto/100)))}
''')