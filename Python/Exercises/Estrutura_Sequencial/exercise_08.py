while True:
    try:
        valorHora = float(input("\nQuanto ganha por hora? "))
        horasTrabalhadas = float(input("\nQuantas horas trabalhou no mes? "))
        break
    except ValueError:
        print("Digite um numero valido!")
print(f"Salario: R${horasTrabalhadas * valorHora}")