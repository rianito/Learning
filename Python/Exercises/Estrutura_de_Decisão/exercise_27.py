'''
27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra 
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a 
quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago 
pelo cliente.
'''

frutas = {
    "morangos": [0.0,2.5,2.2],
    "macas": [0.0,1.8,1.5]
}
peso = 0.0
valor = 0.0

for i in frutas:
    frutas[i][0] = float(input(f"Digite o kg de {i}: "))
    peso += frutas[i][0]
    if frutas[i][0] > 5:
        frutas[i][0] *= frutas[i][2]
    else:
        frutas[i][0] *= frutas[i][1]
    valor += frutas[i][0] 

if peso > 8 or valor > 25:
    valor*=0.9

print(f"valor a ser pago: {valor}")