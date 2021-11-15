f = open(".chave.txt","r")
chave = f.read()
f.close()
f = open("texto.txt","r")
texto = f.read()
f.close()

#Mudei para o split do Python

#def split_do_rian(string,separator):
#    result = []
#    handle = ""
#    for i in string:
#        if i == separator:
#            result.append(handle)
#            handle = ""
#        else:
#            handle = handle + i
#    return result

while True:
    resposta = input('''
    1 - CRIPTOGRAFAR
    2 - DESCRIPTOGRAFAR
    3 - TROCAR CHAVE
    OUTRO - SAIR

    ''')

    if resposta == '1':
        f = open('texto.txt','w')
        for i in texto:
            f.write(f"{ord(i)+int(chave)} ")
        f.close()
    elif resposta == "2":
        texto = texto.split(" ")
        for i in texto:
            f = open('texto.txt','w')
            f.write(f"{chr(int(i)-int(chave))}")
        f.close()
    elif resposta == "3":
        f = open(".chave.txt","w")
        f.write(input("DIGITE A NOVA CHAVE (APENAS NÚMEROS): "))
        f.close()
    else:
        break
