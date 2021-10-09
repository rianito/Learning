f0 = open(".chave.txt","r")
f1 = open("texto.txt","r")
chave = f0.read()
texto = f1.read()
f1 = open("texto.txt","w")


''' Mudei para o split do Python

def split_do_rian(string,separator):
    result = []
    handle = ""
    for i in string:
        if i == separator:
            result.append(handle)
            handle = ""
        else:
            handle = handle + i
    return result
'''

while True:
    resposta = input('''
    1 - CRIPTOGRAFAR
    2 - DESCRIPTOGRAFAR
    3 - TROCAR CHAVE
    OUTRO - SAIR

    ''')

    if resposta == "1":
        for i in texto:
            f1.write(f"{ord(i)+int(chave)} ")
    elif resposta == "2":
            texto = texto.split(" ")
            for i in texto:
                f1.write(f"{chr(int(i)-int(chave))}")
    elif resposta == "3":
        f0 = open(".chave.txt","w")
        f0.write(input("DIGITE A NOVA CHAVE (APENAS NÚMEROS): "))
    else:
        break