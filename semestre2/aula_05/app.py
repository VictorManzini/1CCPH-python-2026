# Aula 05 semestre 2. Introdução a Programação Orientada a Objeto
from aluno import Aluno
from disciplina import Disciplina

# CRIAR / INSTANCIAR 1 ALUNO
aluno1 = Aluno("Victor", "123456", "Ciência da Computação")

# CRIAR / INSTANCIAR 2 Disciplinas 

prompt_ia = Disciplina("Prompt IA", "Jorge")
sers = Disciplina("Soluções Renováveis", "André")

# MATRICULAR O ALUNO NAS DISCIPLINAS 
aluno1.matricular(prompt_ia)
aluno1.matricular(sers)

# ADICIONAR NOTA DO ALUNO REFERENTE A DISCIPLINA
aluno1.adicionar_nota(prompt_ia, 10)
aluno1.adicionar_nota(prompt_ia, 8)
aluno1.adicionar_nota(sers, 5)
aluno1.adicionar_nota(sers, 3)

print(aluno1.calcular_media_d(prompt_ia))