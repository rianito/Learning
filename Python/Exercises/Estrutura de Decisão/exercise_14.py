'''
14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o 
conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

notas = []
media = 0
conceito = ["",""]

for i in range(3):
  notas.append(float(input("Digite uma nota: ")))

for i in notas:
  media += i
media /= len(notas)

if media >= 9:
  conceito = ["A","Aprovado"]
elif media >= 7.5:
  conceito = ["B","Aprovado"]
elif media >= 6:
  conceito = ["C","Aprovado"]
elif media >= 4:
  conceito = ["D","Reprovado"]
else:
  conceito = ["E","Reprovado"]

print(f"Media: {media}\nConceito: {conceito[0]}\nResultado: {conceito[1]}")