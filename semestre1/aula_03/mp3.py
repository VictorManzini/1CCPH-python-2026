# Importa a biblioteca pygame para tocar o arquivo MP3
import pygame 
# Time importa sleep que é o tempo que o programa vai esperar para finalizar a execução
import time 
from time import sleep

file = "Nutshell.mp3"
#Inicializa o pygame e o mixer
pygame.init()
pygame.mixer.init()
# Carrega o arquivo mp3 e toca a música
pygame.mixer.music.load(file)
pygame.mixer.music.play()

print("""A música está tocando...
              
Pressione ctrl + c para encerrar a musica.
              
              """)
# get_busy() retorna True se a musica ainda está tocando e False quando ela terminou
try: 
    while pygame.mixer.music.get_busy():
        #Limita quantas vezes o loop é executado por segundo, nesse caso 10 vezes por segundo
        pygame.time.Clock().tick(10)
        #Permite que o pygame processe os eventos, como o fechamento da janela ou a interrupção do programa
        pygame.event.pump()
except KeyboardInterrupt:
    pygame.mixer.music.stop()
    print("Música encerrada")


