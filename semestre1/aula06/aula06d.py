# Aula de matriz
matriz =[]
for i in range(4): #range 4 define quantas linhas vão ter 
    linha = []
    for j in range(5): #range 5 define qunantas casas as linhas vão ter 
        linha.append(i * 5 + j + 1)
    matriz.append(linha) #Adiciona a lista linha inteira como um elemento da matriz

for linha in matriz: #printa a lista com colunas e linhas
    print(linha)