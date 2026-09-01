usuarios = {
    "ana": 5, 
    "bruno": 0, 
    "carla": 3
}

for usuario, acesso in usuarios.items():

    if acesso == 0:
        del usuarios[usuario]

print(usuarios)