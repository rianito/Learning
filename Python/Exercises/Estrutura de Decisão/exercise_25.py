'''
25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a 
pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como 
"Assassino". Caso contrário, ele será classificado como "Inocente".

'''

resultado = 0

perguntas = [
    "Telefonou para a vitima?",
    "Esteve no local do crime?",
    "Mora perto da vitima?",
    "Devia para a vitima?",
    "Ja trabalhou com a vitima?"
    ]

for i in perguntas:
    resposta = input(i+" ")
    if resposta.upper() == "SIM":
        resultado += 1
        
if resultado > 4:
    print("Assasinso")
elif resultado > 2:
    print("Cumplice")
elif resultado > 1:
    print("Suspeita")
else:
    print("Inocente")
