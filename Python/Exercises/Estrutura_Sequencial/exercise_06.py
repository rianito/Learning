while True:
    try:
        raio = float(input("\nInsira o raio do circulo: "))
        break
    except ValueError:
        print("Digite um numero valido.")
print(raio*raio*3.14)