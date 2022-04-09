while True:
    salario_bruto = float(input("Ganho por hora: ")) * float(input("Horas trabalhadas: "))
    print(f"+ R${salario_bruto:12} Salario bruto\n- R${salario_bruto*0.11:12} IR\n- R${salario_bruto*0.08:12} INSS\n- R${salario_bruto*0.05:12} Sindicato\n= R${salario_bruto-(salario_bruto*0.11+salario_bruto*0.08+salario_bruto*0.05):12} Salario liqiuido")
