'''
4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

vogais = ["A","a","E","e","I","i","O","o","U","u"]

while True:
    letra = input("Digite uma letra: ")
    if letra == "PARAR":
        break
    achou = False
    for i in vogais:
        if letra == i:
            achou = True
            break
    if achou:
        print("\nFoi uma vogal\n")
    else:  
        print("\nFoi uma consoante\n")