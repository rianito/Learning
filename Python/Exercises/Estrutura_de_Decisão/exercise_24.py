'''
24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação 
deve ser acompanhado de uma frase que diga se o número é:
a. par ou ímpar;
b. positivo ou negativo;
c. inteiro ou decimal.

'''

def isdigitDiferenciado(arg1):
    permitidos = ['0','1','2','3','4','5','6','7','8','9','-']
    for i in arg1:
        achou = False
        for ii in permitidos:
            if i == ii:
                achou = True
        if not achou:
            return False
    return True

numeros = []

for i in range(2):
    while True:
        numero = input(f"Digite o numero {i+1}: ")
        if isdigitDiferenciado(numero):
            numeros.append(float(numero))
            break
        else:
            print("Digite apenas numeros.")

while True:
    
    operacao = input("Deseja somar,subtrair,multiplicar ou dividir? ").upper()
    
    if operacao == "SOMAR":
        numeros[0] += numeros[1]
        break
    elif operacao == "SUBTRAIR":
        numeros[0] -= numeros[1]
        break
    elif operacao == "MULTIPLICAR":
        numeros[0] *= numeros[1]
        break
    elif operacao == "DIVIDIR":
        numeros[0] /= numeros[1]
        break
    else:
        print("Digite uma operacao valida.")


print(f"Resultado: {numeros[0]}")

if numeros[0]%2 == 0:
    print("Par")
else:
    print("Impar")

if numeros[0] > 0:
    print("Positivo")
else:
    print("Negativo")

if numeros[0] == int(numeros[0]):
    print("Inteiro")
else:
    print("Decimal")