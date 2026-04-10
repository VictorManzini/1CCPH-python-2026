# Calculadora - exercicio da aula 03 

print("""
      ------ CALCULADRA INICIADA ------
      """)

instructions = input("Deseja ver as instruções do programa? (y/n) ")
if instructions.lower() == "y":
    print(""" 
1º digite o primeiro número. 
2º digite o operador matemático que deseja utilizar (+ - * / %)
3º digite o segundo número.
""")

def calcular(n1, n2, operador):
    if operador == "+":
        return n1 + n2
    elif operador == "-":
        return n1 - n2
    elif operador == "*":
        return n1 * n2
    elif operador == "/":
        if n2 == 0:
            return "Erro: divisão por zero"
        return n1 / n2
    elif operador == "%":
        return n1 % n2
    
while True: 
    n1 = float(input("Digite o primeiro número: "))
    operador = input("Digite o operador matemático: ")
    n2 = float(input("Digite o segundo número: "))

    print(calcular(n1, n2, operador))

    continuar = input("Deseja continuar (y/n)? ")
    if continuar.lower() == "n":
        print(""" 
    ------ PROGRAMA ENCERRADO ------
              """)
        break 