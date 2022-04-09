resultado = 0
for i in range(2):
    while True:
        try:
            resultado += float(input(f"\nDigite o {i+1}o numero: "))
            break
        except ValueError:
            print("Digite um numero valido.")
print(resultado)