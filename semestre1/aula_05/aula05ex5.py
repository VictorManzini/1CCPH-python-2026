n = int(input("Digite a quantidade de nomes que deseja colocar na lista: "))
nomes = []

for i in range(n):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

nomes.reverse()
print(nomes)