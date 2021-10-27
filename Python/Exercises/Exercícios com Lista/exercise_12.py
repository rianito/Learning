'''
12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos 
com mais de 13 anos possuem altura inferior à média de altura desses alunos. 
'''
import random

def gerarAlunos(quantidade):
    handle = []
    for i in range(quantidade):
        handle.append({'idade':random.randrange(10,18),'altura':round(random.uniform(1.5,1.9),2)})
    return handle

alunos = gerarAlunos(30)

def calcularMedia(lista):
    media = 0
    for i in lista:
        media += i['altura']
    media /= len(lista)

    return media

media = calcularMedia(alunos)
for i in alunos:
    if i['idade'] < 13 and i['altura'] < media:
        print(i)
