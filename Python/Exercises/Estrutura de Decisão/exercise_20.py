'''
20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média 
alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

media = 0

for i in range(3):
  media += (float(input("Digite uma nota: ")))
media /= 3
media = round(media,2)
if media == 10:
  print(f"Aprovado com Distincao {media}")
elif media >= 7:
  print(f"Aprovado {media}")
else:
  print(f"Reprovado {media}")