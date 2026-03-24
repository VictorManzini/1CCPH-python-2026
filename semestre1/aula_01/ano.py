
while True:
    ano_atual = int(input("Digite o ano atual: "))
    if ano_atual < 2026 or ano_atual > 2026: 
        print("Ano atual incorreto. Tente novamente.")
        continue 

    while True:
        ano_nascimento = int(input("Digite o ano do seu nascimento: "))
        if ano_nascimento < 1900:
            print("Impossivel, você está morto kkkkkkk. Tente novamente.")
            continue
        break

    idade = ano_atual - ano_nascimento 
    print("Você tem " + str(idade) + " anos de idade")
    break
 

#O codigo acima é uma versão com loop do que fizemos em aula: 
# ano_atual = int(input("Digite o ano atual: "))
# ano_nascimento = int(input("Digite o ano do seu nascimento: "))
# idade = ano_atual - ano_nascimento
# print("Você tem " + str(idade) + " anos de idade")