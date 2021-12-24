import random
lista = [0]*100

for i in range(1000):
    lista[random.randrange(0,10,1)+random.randrange(0,10,1)] += 1

for i in range(0,100):
    print(f"{i}: ",end = "")
    for ii in range(lista[i],0,-1):
        print("|",end = "")
    print(f"\n{lista[i]}\n")