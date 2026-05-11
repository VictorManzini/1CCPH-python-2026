import random

num = int(input("Digite um valor inteiro maior que 0: "))

for i in range(int(num)):
    numero = random.uniform(1, 1000)
    print(f"{numero:.2f}")