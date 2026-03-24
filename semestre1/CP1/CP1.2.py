colaborador = input("Digite o nome do colaborador: ")
horas_trab = int(input("Digite o número de horas trabalhadas (digite apenas números) : "))
valor_hora = float(input(f"Digite o valor da hora de trabalho do(a) colaborador(a) {colaborador} (digite apenas números): "))
bonus = float(input(f"Digite o valor do bônus (em reais) do(a) colaborador(a) {colaborador} (digite apenas números): "))
desc = float(input(f"Digite o desconto do(a) colaborador(a) {colaborador} digite apenas números: "))

Salário_bruto = float(horas_trab) * float(valor_hora) + float(bonus)
Salário_liquido = float(Salário_bruto) - float(desc)

print(f"""Colaborador(a): {colaborador}
Salário bruto: {Salário_bruto:.2f} R$ 
Salário líquido: {Salário_liquido:.2f} R$""")