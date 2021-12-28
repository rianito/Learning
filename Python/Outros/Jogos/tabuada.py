import random
import time

numeros = range(1,10,1)
pontos = 0
inicio = time.time()
jogador = input("Digite seu nome: ")
for i in range(10):
    conta = random.choices(numeros,  k = 2)
    print(f"\n{conta[0]} * {conta[1]} = ",end="")
    if input() == str(conta[0] * conta[1]):
        print("acertou")
        pontos += 1
    else:
        print("errou")
inicio = format((time.time()-inicio),".2f")
print(f"\n{jogador} fez {pontos} pontos em {inicio} segundos.")
