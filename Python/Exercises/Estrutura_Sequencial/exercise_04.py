resultado = 0
for i in range(4):
    while True:
        try:
            resultado += float(input(f"digite a {i+1}a nota: "))
            break
        except ValueError:
            print("Digite um numero valido.")
print(f"media: {resultado / 4}")