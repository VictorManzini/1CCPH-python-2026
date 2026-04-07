# FUNÇÃO COM PARAMETRO SEM RETORNO

def boas_vindas(nome):
    print(f"Olá, {nome}! Seja bem-vindo! ")

nome_digitado = input("Digite o seu nome: ")
boas_vindas(nome_digitado)

# FUNÇÃO COM PARAMETRO E COM RETORNO
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma #return apenas retorna a informação, não exibe

resultado_soma = soma (5,9)
print(resultado_soma)
print(type(nome_digitado))

#soma(5, 9)
#type(nome_digitado) # também retorna a informação e não exibe, é preciso um print() para ambos