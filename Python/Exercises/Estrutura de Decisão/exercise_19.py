'''
19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas 
e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 
e 16
'''

numero = int(input("Digite um numero inteiro menor que 1000: "))
numerodigitado = numero
info = [0,0,0]

while numero > 0:
    if numero >= 100:
        numero -= 100
        info[0] += 1
    elif numero >= 10:
        numero -= 10
        info[1] += 1
    else:
        info[2] = numero
        break

print(f"{numerodigitado} = {info[0]} centenas, {info[1]} dezenas e {info[2]} unidades.")