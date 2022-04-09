'''
16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 
3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

tamanho = float(input("Tamanho em metros quadrados: "))
latas = 0
while tamanho > 0:
    latas += 1
    if tamanho >= 54:
        tamanho -= 54
    else:
        tamanho = 0

print(f"Latas necessárias: {latas}\nPreço: {latas*80}")
