import random 

n = int(input("Digite um número inteiro: "))
vetor = []

for i in range(n):
    num = random.randint(1, 10)
    vetor.append(num)
print(f"Vetor sem inversão: {vetor}")

for j in range(n//2):
    vetor[j], vetor[n-1-j] = vetor[n-1-j], vetor[j]

print(f"Vetor invertido: {vetor}")