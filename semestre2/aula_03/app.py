from model import model_lead
from time import sleep
import control

def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    company = input("Empresa: ")
    stage = input("Estágio de vendas: ")

    if not name or not email or "@" not in email:
        print("Nome e/ou e-mail válido são obrigatórios")
        return

    # precisar chamar model para modelar os dados
    print(model_lead(name, company, email, stage))

    # depois de modelado...
    # vou precisar chamar control.py para enviar os dados modelados para o banco de dados json
    control.create_lead(model_lead(name, company, email, stage))


def list_leads():
    leads = control.read_leads()

    if not leads:
        print("nenhum lead ainda")
        return

    print("\n# | Nome                 | Empresa           | E-mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d}| {lead["name"]:<20} | {lead["company"]:<17} | {lead["email"]:<20} ")

def search_leads():
    query = input("Buscar por: ").strip().lower()
    if not query:
        print("Consulta vazia... ")
        sleep(0.5)
        return
    
    # Nesse momento, irei enviar minha busca para control
    # o control.read_leads_search() irá reetornar um array com os leads encontrados
    leads_finded = control.read_leads_search(query)
    print("\n# | Nome                 | Empresa           | E-mail")
    for i, lead in enumerate(leads_finded):
        print(f"{i:02d}| {lead["name"]:<20} | {lead["company"]:<17} | {lead["email"]:<20} ")
    sleep(0.5)


def export_leads():
    print("Export CSV...")
    sleep(0.5)

def main():
    while True:
        print("\nMini CRM - 1ª aula - (adicionar/listar)")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar (nome/e-mail/empresa)")
        print("[4] Esxportar para CSV")
        print("[0] Sair do programa")

        opt = input("Escolha uma ação: ").strip()
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Até mais")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()