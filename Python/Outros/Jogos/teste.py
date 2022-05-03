from asyncore import write
import random
import os
import json

palavras = [
    "macaco", "girafa", "cavalo",
    "cachorro", "gato", "gorila",
    "tatu", "cobra", "mosca",
    "mamute", "mosquito"
    ]

def clearConsole():
    tipo = os.name
    if tipo == "nt":
        os.system("cls")
    elif tipo == "posix":
        os.system("clear")
    else:
        print("Nao foi possivel identificar seu sistema operacional.")

def showResult(descobrindo):
    result = ""
    for letra in descobrindo:
        result += f"{letra} "
    return result

def criarsave():
    template = {
        "user_words" : [],
        "scoreboard" : []
        }
    try:
        f = open("dados.txt", "w")
        f.write(json.dumps(template))
        f.close()
        return True
    except Exception:
        return False

def carregarsave():
    try:
        f = open("dados.txt", "r")
        dados = json.loads(f.read())
        f.close()
        print("Save encontrado.")
        return dados
    except FileNotFoundError:
        print("Save nao foi encontrado, criando um novo save...")
        if criarsave():
            return carregarsave()
        print("Nao foi possivel criar o save.")
    except json.JSONDecodeError:
        print("O arquivo esta corrompido ou nao esta no formato JSON. Deseja resetar? S/N")
        while True:
            resposta = input().upper()
            if resposta == "S":
                print("Resetado.")
                return "teste"
            elif resposta == "N":
                return None
            else:
                print("Digite uma opcao valida.")

while True:
    clearConsole()
    dados = carregarsave()
    tentativas = 3
    pontos = 0
    nome = input("Digite seu nome: ")
    palavra = random.choice(palavras)
    descobrindo = ["_"]*len(palavra)

    while tentativas > 0:
        while True:
            letra = input("Escolha uma letra: ").lower()
            if letra.isnumeric() or len(letra) > 1:
                print("Digite apenas uma letra.")
                continue
            break

        for i in range(len(palavra)):
            if palavra[i] == letra:
                descobrindo[i] = letra
                pontos += 1
        
        if pontos == len(palavra):
            print(f"Você venceu, {nome}!")
            print(palavra)
            break
        
        print(showResult(descobrindo))
        
    option = input("Jogar novamente? Sim - S / Não - Outro").upper()
    if option != "S":
        break