# Programa de comparação de números aleatórios - execício da aula 03

import random 

def gerar_numero():
    return random.randint(1, 20)

def comparar(num1, num2):
    if num1 > num2:
        return f"{num1} é maior que {num2}"
    elif num1 < num2: 
        return f"{num2} é maior que {num1}"
    else:
        return "Os dois são iguais"
    
num1 = gerar_numero()
num2 = gerar_numero()

print(f"Número 1: {num1}")
print(f"Número 2: {num2}")
print(comparar(num1, num2))
