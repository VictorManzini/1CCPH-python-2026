while True:
    inteiro = int(input("Digite um número inteiro: "))
    if inteiro <= 0:
        print("O número precisa ser positivo")
        continue
    else:
        for i in range(1, inteiro + 1): 
            if inteiro % i == 0:
                print(i)
        break