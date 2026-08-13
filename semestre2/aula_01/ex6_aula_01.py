import random
while True: 
    inteiro = int(input("Digite um número inteiro: "))
    if inteiro <= 0:
        print("O número precisa ser positivo")
        continue 
    else: 
        numeros = []
        for i in range(inteiro):
            numeros.append(random.randint(1, 1000))
        print(numeros)
        break