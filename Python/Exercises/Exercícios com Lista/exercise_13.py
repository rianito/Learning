'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ). '''

meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
temperaturas = []
for i in meses:
    temperaturas.append(int(input(f'{i}:')))

media = sum(temperaturas)/len(temperaturas)

for i in range(len(meses)):
    if temperaturas[i] > media:
        print(f'{i} - {meses[i]} : {temperaturas[i]}')
