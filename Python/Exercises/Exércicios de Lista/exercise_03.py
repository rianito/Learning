'''
3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

media = 0
notas = []

for i in range(4):
    notas.append(int(input("Digite uma nota: ")))

for i in notas:
    print(i)
    media += i

print(media/len(notas))
