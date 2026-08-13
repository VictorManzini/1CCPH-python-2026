import os 

os.system('clear')
print("\n")

emails = {}

def inserir(email):
    entrada = input("Digite os emalis separados por vírgula: ")
    lista_emails = entrada.split(",")
    lista_emails = [email.strip() for email in lista_emails]
    print(lista_emails)
    contagem_dominios = {}
    lista_usuarios = []
    for email in lista_emails:
        usuario, dominio = email.split("@")
        contagem_dominios[dominio] = contagem_dominios.get(dominio, 0) + 1
        lista_usuarios.append(usuario)
    tupla_usuarios = tuple(lista_usuarios)
    print("Primeiro: ", tupla_usuarios[0])
    print("Último: ", tupla_usuarios[-1])
    lista_troca = list(tupla_usuarios)
    lista_troca[0], lista_troca[-1] = lista_troca[-1], lista_troca[0]
    tupla_trocada = tuple(lista_troca)
    print("Relatório: ")
    print("Quantidade de emails por domínio: ")
    for dominio, quantidade in contagem_dominios.items():
        print(f"{dominio}: {quantidade}")
    print("Lista de usuários: ", tupla_usuarios)
    print("Lista de usuários com posições trocadas: ", tupla_trocada)

inserir(emails)