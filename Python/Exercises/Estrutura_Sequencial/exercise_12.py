while True:
    try:
        altura = float(input(f"Digite sua altura: "))
        break
    except ValueError:
        print("Digite um numero valido!")
print(f"Peso ideal: {round((72.7*altura) - 58,4)}")