# reajuste de salário - exercício da aula 03

print("""
            BEM-VINDO!
VAMOS CALCULAR O REAJUSTE DE SALÁRIO
      """)

def calcular(salario):
    if salario <= 279:
        percentual = 0.20
    elif salario >= 280 and salario <= 699:
        percentual = 0.15
    elif salario > 700 and salario <= 1499:
        percentual = 0.10
    else:
        percentual = 0.05
    aumento = salario * percentual
    novo_salario = salario + aumento
    return novo_salario, aumento, percentual
    
salario = float(input("Digite o seu salário: "))
novo_salario, aumento, percentual = calcular(salario)

print(f"Salário sem reajuste {salario}")
print(f"Percentual aplicado: {percentual * 100:.0f}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Salário reajustado: R$ {novo_salario:.2f} ")
