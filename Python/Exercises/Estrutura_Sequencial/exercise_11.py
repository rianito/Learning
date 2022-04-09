def checktype(value,type):
    info = {
        "int" : "Digite um inteiro valido!",
        "float" : "Digite um real valido!"
    }
    while True:
        try:
            return type(value)
        except ValueError:
            print(info[type.__name__])
            return checktype(input("\nDigite novamente: "),type)
int_0 = checktype(input("\nDigite um numero inteiro: "),int)
int_1 = checktype(input("\nDigite outro numero inteiro: "),int)
real = checktype(input("\nDigite um numero real: "),float)
print(int_0*2*int_1/2,int_0*3+real,real*real*real)