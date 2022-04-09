while True:
    try:
        peso = float(input("Digite o peso: "))
        if peso > 50:
            excesso = peso - 50
            multa = excesso * 4
            print(f"\nExcesso: {excesso}kg\nMulta: R${multa}\n")
        else:
            print(f"\nTudo okay.\n")
    except ValueError:
        print("\nDigite um numero valido.\n")
