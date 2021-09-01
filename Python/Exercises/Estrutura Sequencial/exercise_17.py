'''
17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da 
área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que 
a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam 
R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e 
sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
areadigitada = float(input("Tamanho em metros quadrados: "))
area = areadigitada
latas = 0
galoes = 0

while area > 0:
    if area >= 108:
        latas += 1
        area -= 108
    else:
        latas += 1
        area = 0

print(f"\nApenas em latas:\n{latas} latas\nValor: R${latas*80}\n")

area = areadigitada
latas = 0

while area > 0:
    if area >= 21.6:
        galoes += 1
        area -= 21.6
    else:
        galoes += 1
        area = 0

print(f"\nApenas em galoes:\n{galoes} galoes\nValor: R${galoes*25}\n")

galoes = 0
area = areadigitada
while area > 0:
    if area >= 108:
        latas += 1
        area -= 108
    elif area >= 21.6:
        galoes += 1
        area -= 21.6
    else:
        galoes += 1
        area = 0

print(f"\nEm latas e galões: {latas} latas e {galoes} galoes \nValor: R${galoes*25+latas*80}\n")