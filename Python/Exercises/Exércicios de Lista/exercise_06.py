'''
6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene 
num vetor a média de cada aluno, imprima o número de alunos com média maior ou 
igual a 7.0.
'''

medias = []

for i in range(10):
    media = 0
    for ii in range(4):
        media += float(input(f"Digite a nota {ii+1} do aluno {i+1}: "))
    medias.append(media/4)

for i in range(len(medias)):
    if medias[i] >= 7:
        print(f"Aluno {i+1}: {medias[i]}")