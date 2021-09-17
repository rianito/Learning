'''
2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
'''

while True:

    info = {
        "NOME DE USUARIO": "",
        "SENHA": ""
    }

    for i in info:
        info[i] = input(f"{i}: ")

    if info["NOME DE USUARIO"] == info["SENHA"]:
        print("A senha nao pode ser o nome de usuario.")
    else:
        break