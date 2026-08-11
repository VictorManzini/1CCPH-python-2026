# Aula 02 Dicionários e Tuplas 11/08/2026

eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {'one': 'uno', 
          'two': 'dos', 
          'three': 'tres'
}
print(eng2sp)
print(eng2sp['two'])


#OPERADOR IN

print('one' in eng2sp)

# Verificar os valores do dic 
valores = eng2sp.values()
print('uno' in valores)

#CONTADOR DE LETRAS

def count_letters(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

dict_contagem = count_letters("FIAP")
print(dict_contagem)