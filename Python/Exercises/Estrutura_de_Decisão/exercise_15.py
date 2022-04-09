'''
15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um 
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''

triangulo = []

for i in range(3):
    triangulo.append(float(input("Digite um lado do triangulo: ")))

iguais = 0
for i in triangulo:
    for ii in triangulo:
        if i == ii:
            iguais += 1

if iguais == 9:
    print("Triangulo equilatero")
elif iguais == 5:
    print("Triangulo isosceles")
else:
    print("Triangulo escaleno")