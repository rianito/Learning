'''
4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''
vowels = "AEIOU"

def search(char):
    for i in range(len(vowels)):
        if vowels[i] == char:
            return "Foi uma vogal"
    return "Foi uma consoante"

print("Digite uma letra: ")
while True:
    char = input().upper()
    if char.isnumeric() or len(char) > 1 or char == " ":
        print("Digite apenas uma letra.")
        continue
    print(search(char))