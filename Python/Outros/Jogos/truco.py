valor = ["4","5","6","7","Q","J","K","A","2","3"]
naipe = ["O","E","C","P"]

baralho = []

for i in naipe:
    for ii in valor:
        baralho.append(i+ii)

print(baralho)