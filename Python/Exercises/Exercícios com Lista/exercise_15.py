'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

    Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem; '''

valores = []

while True:
    resposta = int(input('digite um valor: '))
    if resposta != -1:
        valores.append(resposta)
    else:
        break
print('')
print(len(valores),end = '\n\n')

for i in valores:
    print(i,end = ' ')
print('\n')
for i in range(len(valores)-1,-1,-1):
    print(valores[i])
print('')
print(sum(valores),end = '\n\n')
media = sum(valores)/len(valores)
print(media,'\n')

quantidade = 0
abaixo = 0
for i in valores:
    if i > media:
        quantidade += 1
    if i < 7:
        abaixo += 1
print(f'{quantidade}\n\n{abaixo}',end = '\n')
