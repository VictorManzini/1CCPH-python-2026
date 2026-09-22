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
    print(f"\n# | {"Nome":<20} | {"Empresa":<17} | E-mail")
    for i, lead in enumerate(leads_finded):
        print(f"{i:02d}| {lead["name"]:<20} | {lead["company"]:<17} | {lead["email"]:<20} ")
    sleep(0.5)

def edit_lead():
    leads = control.read_leads()
    if not leads:
        print("Nenhum lead ainda...")
        return

    list_leads()

    try:
        index = int(input("Digite o numero do lead que deseja alterar: "))
    except ValueError: 
        print("Digite um número válido")
        return
    print("O que deseja atualizar? ")
    print("[1] Nome [2] Empresa [3] E-mail [4] Estágio")
    escolha = input("Escolha: ").strip()

    campos = {"1": "name", "2": "company", "3": "email", "4": "stage"}
    if escolha not in campos.keys(): 
        print("Opcao inválida...")
        return

    novo_valor = input("Digite o novo valor: ")

    new_data = {index: novo_valor}
    control.update_lead(campos[escolha], new_data)

def remove_lead():
    pass

def export_leads():
    path_csv = control.export_csv()
    print(path_csv)

    if path_csv in None: 
        print("Não foi possível exportar os leads para CSV")
    else:
        print(f"CSV exportado para {path_csv}")
    sleep(0.5)

def main():
    while True:
        print("\nMini CRM - 1ª aula - (adicionar/listar)")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar (nome/e-mail/empresa)")
        print("[4] Atualizar lead")
        print("[5] Deletar lead")
        print("[6] Esxportar para CSV")
        print("[0] Sair do programa")

        opt = input("Escolha uma ação: ").strip()
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            edit_lead()
        elif opt == "5":
            pass
        elif opt == "0":
            print("Até mais")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()