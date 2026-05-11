import random 

A = []
B = []
C = []

for i in range(2):
    linha = []
    for j in range(3):
        linha.append(random.randint(1, 10))
    A.append(linha)

for i in range(2):
    linha = []
    for j in range(3):
        linha.append(random.randint(1, 10))
    B.append(linha)

for i in range(2):
    linha = []
    for j in range(3):
        linha.append(A[i][j] + B[i][j])
    C.append(linha)

for linha in C:
    print(linha)