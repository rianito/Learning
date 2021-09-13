'''
4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

vogais = ["A","E","I","O","U"]

letra = input("Digite uma letra: ").upper()
achou = False
for i in vogais:
    if letra == i:
        achou = True
        break

print("\nFoi uma vogal\n") if achou else print("\nFoi uma consoante\n")