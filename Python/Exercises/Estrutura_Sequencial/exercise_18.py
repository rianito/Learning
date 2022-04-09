'''
18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link 
de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link 
(em minutos).
'''

tamanho = float(input("Digite o tamanho do arquivo em MB: "))
velocidade = float(input("Digite sua velocidade de conexao em Mbps: "))

print(f"Tempo aproximado de download: {(((tamanho*1024*1024*8)/1000000)/velocidade)/60} minutos")