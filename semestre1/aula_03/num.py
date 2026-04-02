# Exercicio da aula 3. Criar um programa para identificar se um número é par ou ímpar.

print("Vamos descobrir se um número é par ou ímpar!")

while True:

    num = int(input("Digite um número inteito: "))

    if num % 2 == 0: 
        print(f"O número {num} é par!")
    else:
        print(f"O número {num} é ímpar!")

    resposta = input("Deseja continuar? (s/n) ")
    if resposta.lower() == "s":
        continue 
    else: 
        print("""
              
              
              Obrigado! Até a próxima!
              
              
            """)
        break
    