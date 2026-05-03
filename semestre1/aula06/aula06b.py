#Atividade 1 
import numpy as np

nomes = ["Victor", "Sarah", "Adriana", "Roberto"]

for i in range(len(nomes)):
    for j in range(i + 1, len(nomes)):
        print(f"{nomes[i]}, {nomes[j]}")
