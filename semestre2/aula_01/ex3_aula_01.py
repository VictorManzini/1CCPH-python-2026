
while True: 
    numeros = []
    inteiro = int(input("Digite um número inteiro: "))
    if inteiro <= 0:
        print("O número precisa ser positivo")
        continue
    else: 
        for i in range(inteiro):
            numero = i + 1
            numeros.append(numero)
        print(f"A soma de 1 até {inteiro} é: ",sum(numeros))   
        break 