# Aula 01 semestre 2 04/08/2026 - GoodWe, Matrizes e exercícios

endpoint = ["/login", "/produtos", "/pedidos"]

status = [
    [200, 200, 401, 200, 500], #requests do endpoint /login
    [200, 200, 200, 200, 200], #requests do endpoint /produtos
    [201, 500, 502, 201, 500]  #requests do endpoint /pedidos
]

def is_sucesso(codigo):
    """2xx = sucesso. Qualquer outra faixa (4xx, 5xx) = erro."""
    return 200 <= codigo < 300
 
 
def tem_erros_consecutivos(linha):
    """Percorre pares vizinhos (i, i+1) procurando dois erros seguidos."""
    for i in range(len(linha) - 1):
        if not is_sucesso(linha[i]) and not is_sucesso(linha[i + 1]):
            return True
    return False
 
 
resultados = {}
 
for i, endpoint in enumerate(endpoint):
    linha = status[i]                      # <- aqui está a "linha só"
    total = len(linha)
    sucessos = sum(1 for c in linha if is_sucesso(c))
    erros = total - sucessos
    pct_sucesso = (sucessos / total) * 100
    consecutivos = tem_erros_consecutivos(linha)
 
    if consecutivos:
        classificacao = "CRÍTICO"          # [suposição] CRÍTICO tem prioridade
    elif pct_sucesso >= 80:                # sobre INSTÁVEL — enunciado não
        classificacao = "ESTÁVEL"          # define a prioridade entre as regras
    else:
        classificacao = "INSTÁVEL"
 
    resultados[endpoint] = {
        "pct_sucesso": pct_sucesso,
        "erros": erros,
        "consecutivos": consecutivos,
        "classificacao": classificacao,
    }
 
endpoint_mais_erros = max(resultados, key=lambda e: resultados[e]["erros"])
 
print("=== Relatório por endpoint ===")
for endpoint, dados in resultados.items():
    print(f"{endpoint:12} | sucesso: {dados['pct_sucesso']:5.1f}% | "
          f"erros: {dados['erros']} | {dados['classificacao']}")
 
print(f"\nEndpoint com mais erros: {endpoint_mais_erros} "
      f"({resultados[endpoint_mais_erros]['erros']} erros)")