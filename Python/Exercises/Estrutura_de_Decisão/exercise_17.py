'''
17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este 
ano é ou não bissexto.
'''

ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("O ano e bissexto")
        else:
            print("O ano nao e bissexto")
    else:
        print("O ano e bissexto")
else:
    print("O ano nao e bissexto")