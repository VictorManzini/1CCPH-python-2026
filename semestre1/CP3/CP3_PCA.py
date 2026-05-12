temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

sala_maior_risco = 0
max_criticos = 0

for i, sala in enumerate(temperaturas):
    media = sum(sala) / len(sala)                          
    criticos = sum(1 for t in sala if t >= 33)             

    print(f"Sala {i + 1}")
    print(f"Média: {media}")
    print(f"Registros críticos: {criticos}")

    if criticos > max_criticos:                            
        max_criticos = criticos
        sala_maior_risco = i + 1

print(f"Sala com maior risco: Sala {sala_maior_risco}")