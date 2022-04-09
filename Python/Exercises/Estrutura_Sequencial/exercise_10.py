while True:
    try:
        celsius = float(input("Digite a temperatura em Celsius: "))
        break
    except ValueError:
        print("Digite um numero valido!")
print(f"Fahrenheit: {((celsius / 5) * 9) + 32}")