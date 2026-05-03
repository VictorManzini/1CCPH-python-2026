alunos = int(input("Digita a quantidade de alunos: "))
notas = []
acima = 0 
abaixo = 0
igual = 0 
for n in range(int(alunos)):
    nota = float(input(f"Digite a nota do aluno {n+1}: "))
    notas.append(nota)

media = sum(notas) / alunos
print(f"A média dos alunos é: {media:.2f}")

for nota in notas:
    if nota > media:
        acima += 1
    elif nota == media:
        igual += 1
    else:
        abaixo += 1

print(f"Notas acima: {acima:}")
print(f"Notas abaixo: {abaixo}")
print(f"Notas iguais a média: {igual}")
