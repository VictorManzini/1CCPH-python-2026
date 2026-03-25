colaborador = input("Digite o nome do colaborador: ")
horas_trab = int(input("Digite o número de horas trabalhadas (digite apenas números) : "))
valor_hora = float(input(f"Digite o valor da hora de trabalho do(a) colaborador(a) {colaborador} (digite apenas números): "))
bonus = float(input(f"Digite o valor do bônus (em reais) do(a) colaborador(a) {colaborador} (digite apenas números): "))
desc = float(input(f"Digite o desconto do(a) colaborador(a) {colaborador} digite apenas números: "))

Salário_bruto = horas_trab * valor_hora + bonus
Salário_liquido = Salário_bruto - desc


print(f"""Colaborador(a): {colaborador}
Salário bruto: {Salário_bruto:.2f} R$ 
Salário líquido: {Salário_liquido:.2f} R$""")


# Abaixo temos o bloco antigo, o professor descontou 0.5 pontos pelo mesmo motivo do CP1.py
'''Salário_bruto = float(horas_trab) * float(valor_hora) + float(bonus)
Salário_liquido = float(Salário_bruto) - float(desc)'''

# Bloco abaixo é apenas uma variação do código onde eu coloco o valor sem o bônus para o usuario visualizar
# Feito depois da correção, não foi feita na prova
'''Salário_s_bonus = horas_trab * valor_hora

print(f"""Colaborador(a): {colaborador}
Salário bruto sem bônus: {Salário_s_bonus:.2f} R$
Salário bruto: {Salário_bruto:.2f} R$ 
Salário líquido: {Salário_liquido:.2f} R$""")

'''