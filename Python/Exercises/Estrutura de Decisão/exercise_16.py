'''
16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas 
seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve 
fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
import math

valores = {"a": 0,"b": 0,"c": 0}

for i in valores:
    valores[i] = float(input(f"Digite o valor de {i}: "))
    if valores["a"] == 0:
        print("A equacao nao e do segundo grau.")
        break

if valores["a"] != 0:
    delta = pow(valores["b"],2) - 4 * valores["a"] * valores["c"]
    if delta < 0:
        print("a equacao nao possui raizes reais.")
    elif delta > 0:
        print("x¹ = ",-valores["b"] + math.sqrt(delta) / 2 * valores["a"])
        print("x² = ",-valores["b"] - math.sqrt(delta) / 2 * valores["a"])
    else:
        print("x = ",-valores["b"] + math.sqrt(delta) / 2 * valores["a"])