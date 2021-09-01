'''
18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''

data = input("Digite uma data (dd/mm/aaaa): ")
if data[2] == "/" and data[5] == "/" and len(data) == 10:    
    novadata = data.split("/")
    if int(novadata[0]) <= 31:
        if int(novadata[1]) <= 12:
            if int(novadata[2]):
                print("Data valida")
        else:
            print("Data invalida")
    else:
        print("Data invalida")
else:
    print("Data invalida")