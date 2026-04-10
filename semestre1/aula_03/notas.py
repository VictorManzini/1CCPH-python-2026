# Programa para calclar a média do aluno - Exercício da aula 03
n1 = float(input("Digite a nota do primeiro bimestre: "))
n2 = float(input("Digite a nota do segundo bimestre: "))
n3 = float(input("Digite a nota do terceiro brimestre: "))
n4 = float(input("Digite a nota do quarto bimestre: "))

media = (n1 + n2 + n3+ n4) / 4 
print(f"A média do aluno é: {media:.2f}")

if media >= 6: 
    print("Aluno aprovado!")
elif media >= 5:
    print("Aluno em recuperação!")
else: 
    print("Aluno reprovado...")
