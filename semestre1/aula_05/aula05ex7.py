import random 
vetor = []


for i in range(3):
    linhas = []
    for j in range(4):
        n = random.randint(1,20)
        linhas.append(n)
    vetor.append(linhas)

for linha in vetor:
    print(linha)