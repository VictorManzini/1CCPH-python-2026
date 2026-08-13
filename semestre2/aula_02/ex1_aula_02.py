import os 
os.system("clear")

emails = {}

def inserir(email):
    entrada = input("Digite os emails separados por vírgula: ")
    lista_emails = entrada.split(",")
    lista_emails = [email.strip() for email in lista_emails]
    print(lista_emails)
    contagem_dominios = {}
    for email in lista_emails: 
        user, domain = email.split("@")
        print(f"Usuário: {user} | Domínio: {domain}")
        contagem_dominios[domain] = contagem_dominios.get(domain, 0) + 1
        #contagem_dominios.get(domain, 0) + 1 pega o valor atual da chave domain no dicionário e soma no valor do get
        #contagem_dominios[domain] guarda o resultado acima de volta na mesma chave domain
    print(contagem_dominios)
    return email

inserir(emails)
print(emails)