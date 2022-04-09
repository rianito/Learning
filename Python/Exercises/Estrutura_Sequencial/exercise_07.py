while True:
    try:
        lado = float(input("Digite um lado do quadrado: "))
        break
    except ValueError:
        print("Digite um numero valido.")
print(f"Dobro da area do quadrado: {lado*lado*2}")