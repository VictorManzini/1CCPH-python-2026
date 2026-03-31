#Módulos - Aula 03 31/03/2026
import math

num = 17
raiz = math.sqrt(num)
print(f"A raiz de {num} é {raiz:.2f}") # o :.2f aduciona apenas duas casas decimais após o ponto. Você pode alterar :.xf

graus = 45              #Eu não lembro trigonometria
radiano = graus / 180 * math.pi
seno = math.sin(radiano)
print(seno)

import random

num_rand = random.random()
print(num_rand*10)

num_rand_int = random.randint(1, 10)
print(num_rand_int)

