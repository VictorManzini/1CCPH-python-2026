rodando = True

while rodando:
    print("Hello, World!")

    opcao = input("deseja continuar? (Y/N)").upper()
    if opcao == "N":
        print("Até a próxima!")
        rodando = False
        