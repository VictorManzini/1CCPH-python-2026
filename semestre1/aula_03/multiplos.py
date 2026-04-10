# Programa para verificar se os números são múltiplos - exercício da aula 03

print("Vamos verificar se os numeros são múltiplos")

def multiplos(num1, num2):
    if num1 % num2 == 0:
        return f"{num1} é múltiplo de {num2}."
    elif num2 % num1 == 0:
        return f"{num2} é múltiplo de {num1}."
    else: 
        return f"{num1} e {num2} não são múltiplos."


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print(multiplos(num1, num2))
