# programa para calcular o voto do eleitor 
print("Descubra se você é obrigado a votar ou não!")

ano_nasc = int(input("Digite o seu ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_nasc
print(idade)
if idade >=16 and idade <= 70:
    print("Você não é obrigado a votar, seu voto é opcional!")
elif idade < 16: 
    print("Você não pode votar ainda!")
else: 
    print("Você é obrigado a votar!")
    