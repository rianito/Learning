import random
palavras = ["macaco","teste"]
palavra = random.choice(palavras)
descobrindo = []
achou = 0
antes = 0
for i in range(len(palavra)):
    descobrindo.append("_")
tentativas = 5
while tentativas:
    letra = input("Escolha uma letra: ").upper()
    if len(letra) == 1 and not letra.isdigit():
        for i in range(len(palavra)):
            if letra == palavra[i].upper():
                descobrindo[i] = letra
                achou += 1
        if achou != antes:
            antes = achou
            if achou == len(palavra):
                print("\nVocê ganhou!")
                break
        else:
            tentativas -= 1
            print(f"\nVocê errou! restam {tentativas} tentativas.")
    else:
        print("\nDigite apenas UMA LETRA!")
    print("\n")
    for i in descobrindo:
        print(i,end=" ")
    print("\n")
if tentativas == 0:
    print("\nVocê perdeu troxa!")
else:
    print("\n")