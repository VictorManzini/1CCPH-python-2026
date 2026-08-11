
endpoint = ["/login", "/produtos", "/pedidos"]

status = [
    [200, 200, 401, 200, 500], #requests do endpoint /login
    [200, 200, 200, 200, 200], #requests do endpoint /produtos
    [201, 500, 502, 201, 500]  #requests do endpoint /pedidos
]

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# Função que valida na lista de req de UM endpoint se tem DOIS erros seguidos
def erros_seguidos(respostas_http):
    for i in range(len(respostas_http) - 1):
        codigo_atual = respostas_http[i]
        proximo_codigo = respostas_http[i+1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(proximo_codigo):
            return True
    return False

def analisar_endpoint(respostas_http):
    qtd_sucessos = 0

    for cod_http in respostas_http:
        if eh_sucesso(cod_http):
            qtd_sucessos += 1

    qtd_total_req = len(respostas_http)
    qtd_erros = qtd_total_req - qtd_sucessos

    percentual_sucessos = (qtd_sucessos / qtd_total_req) * 100

    tem_erros_seguidos = erros_seguidos(respostas_http)

    if tem_erros_seguidos:
        classificacao = "CRITICO"
    elif percentual_sucessos >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"

    return(qtd_sucessos, qtd_erros, percentual_sucessos, classificacao)

maior_qtd_erros = -1
endpoitn_maior_erro = ""

for i in range(len(endpoint)):
    nome_endpoint = endpoint[i]
    respostas_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint()

    print(f"Endpoint: {nome_endpoint}")
    print(f"Respostas http: {respostas_endpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"% de sucessos: {percentual}")
    print(f"Classificação: {classificacao}")
    print("-" * 30)
    print()