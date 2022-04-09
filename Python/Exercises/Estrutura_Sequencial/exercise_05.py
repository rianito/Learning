while True:
    try:
        numero = float(input("\nDigite o valor em metros: "))
        break
    except ValueError:
        print("Digite um numero valido.")
print(f"{numero} metros = {numero*100} centimetros.")