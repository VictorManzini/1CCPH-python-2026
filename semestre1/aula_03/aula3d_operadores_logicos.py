# Operadores Lógicos - Aula 3d 31/03/2026

#Lógica E
verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entrar no programa")



# Lógica OU (or)
logica_ou = False or True
print(logica_ou)

# Operador NOT
negacao = not True
print(negacao)

if not verifica_login:
    print("Loga certo aí cara")
