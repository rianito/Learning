while True:
    try:
        fahrenheit = float(input("\nDigite a temperatura em Fahrenheit: "))
        break
    except ValueError:
        print("Digite um numero valido!")
print(f"Celsius: {5*((fahrenheit-32)/9)}")