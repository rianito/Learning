'''
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a. o produto do dobro do primeiro com metade do segundo .
    b. a soma do triplo do primeiro com o terceiro.
    c. o terceiro elevado ao cubo.
'''

int_0 = int(input("Digite um numero inteiro: "))
int_1 = int(input("Digite outro numero inteiro: "))
float_0 = float(input("Digite um numero real: "))
print(f"a: {(int_0*2)+(int_1/2)}\nb: {(int_0*3)+float_0}\nc: {float_0*float_0*float_0}")