while True:
    try:
        altura = float(input(f"Digite sua altura: "))
        break
    except ValueError:
        print("Digite um numero valido!")
print(f"Peso ideal:\nHomem:{round((72.7*altura) - 58,4)}\nMulher:{round((62.1*altura) - 44.7,4)}")
