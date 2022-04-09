while True:
    try:
        numero = float(input("\nDigite um numero: "))
        break
    except ValueError:
        print("Digite um numero valido!")  
print(f"O número informado foi: {numero}")