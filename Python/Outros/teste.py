def acharDiferentes(args):
    diferentes = []
    def achar(lista1,lista2):
        resultados = []
        for i in lista1:
            igual = False
            for ii in lista2:
                if i == ii:
                    igual = True
            if not igual:
                resultados.append(i)
        for i in lista2:
            igual = False
            for ii in lista1:
                if i == ii:
                    igual = True
            if not igual:
                resultados.append(i)
        return resultados
    for i in range(len(args)):
        if i == 0:
            diferentes = achar(args[i],args[i+1])
        elif i > 1:
            diferentes = achar(diferentes,args[i])
    return set(diferentes)
print(acharDiferentes([[3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]]))