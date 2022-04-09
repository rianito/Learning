'''
11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''

vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []

for i in range(10):
    vetor1.append(input(f"Vetor 1 [{i}]: "))
    vetor2.append(input(f"Vetor 2 [{i}]: "))
    vetor3.append(input(f"Vetor 3 [{i}]: "))

for i in range(0,len(vetor1),1):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])

print(vetor4)