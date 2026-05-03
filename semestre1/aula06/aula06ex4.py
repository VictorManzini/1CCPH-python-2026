n = int(input("Digite um número inteiro: "))
vetor_int = []

for i in range(n):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor_int.append(numero)

result = sum((vetor_int))
print(f"A soma dos valores é: {result}")
