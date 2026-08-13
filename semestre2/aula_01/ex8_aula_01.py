linhas = int(input("Número de linhas: "))
colunas = int(input("Número de colunas: "))

print("Preencha a matriz A: ")
A = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"A[{i+1}][{j+1}]: "))
        linha.append(valor)
    A.append(linha)

print("Preencha a matriz B: ")
B = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"B[{i+1}][{j+1}]"))
        linha.append(valor)
    B.append(linha)

C = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(A[i][j] + B[i][j])
    C.append(linha)

print("Matriz soma C: ")
for linha in C:
    print(linha)