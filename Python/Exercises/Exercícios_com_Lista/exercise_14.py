'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". '''

perguntas = ['Telefonou para a vítiNma?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']
positivo = 0

for i in perguntas:

    while True:
        resposta = input(f'{i} ').upper()
        if resposta == 'S':
            positivo += 1
            break
        elif resposta == 'N':
            break
        else:
            print('\nresponda apenas S ou N\n')

if positivo > 4:
    print('Assasino')
elif positivo > 2:
    print('Cúmplice')
elif positivo > 0:
    print('Suspeita')
else:
    print('Inocente')
