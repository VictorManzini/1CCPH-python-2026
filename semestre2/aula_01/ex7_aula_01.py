while True: 
    inteiro = int(input("Digite um número inteiro: "))
    if inteiro <= 0: 
        print("O número precisa ser positivo ")
        continue
    else: 
        vetor = []
        for i in range(inteiro):
            caractere = input(f"Digite o caractere {i+1}: ")
            vetor.append(caractere)

        for i in range(inteiro//2):
            vetor[i], vetor[inteiro - 1 - i] = vetor[inteiro - 1 - i], vetor[i] #serve para inverter a ordem do vetor

        print("Vetor invertido: ", vetor)
        break