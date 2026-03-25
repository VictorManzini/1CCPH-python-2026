
produto = input("Digite o nome do produto: ")
preco_uni = float(input("Digite o valor unitário do produdo (digite apenas números): "))
quant = int(input("Digite a quantidade comrprada de produtos: "))
desconto = float(input("Digite o percentual de descsonto do produto (digite apenas números, ex: 15 para 15%): "))

valor_bruto = preco_uni * quant
desc = desconto / 100
desc_final = valor_bruto * desc
valor_final = valor_bruto - desc_final
print(f"""O produto é: {produto}
O valor bruto é: {valor_bruto:.2f} R$
O desconto é de: {desc_final:.2f} R$ 
O valor final é: {valor_final:.2f} R$""")


# Abaixo é o bloco antigo, o professor descontou 0.5 pontos devido à repetição da definição do tipo de número,
# float ou int
'''valor_bruto = float(preco_uni) * int(quant)
desc = float(desconto) / 100
desc_final = float(valor_bruto) * float(desc)
valor_final = float(valor_bruto) - float(desc_final)'''

