'''
4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
Imprima as consoantes.
'''


vogais = ["A","E","I","O","U"]

lista = []

vogais_achadas = 0

for i in range(10):
    lista.append(input("Digite uma letra: ").upper())

for i in lista:
    vogais_achadas += vogais.count(i)
print(f"consoantes achadas: {len(lista) - vogais_achadas}")