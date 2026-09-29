from disciplina import Disciplina

class Aluno:
    def __init__(self, nome, rm, curso):
        self.nome = nome
        self.rm = rm
        self.curso = curso
        self.disciplinas = []   # Lista de objetos Disciplina
        self.notas_por_disciplina = {}

    def matricular(self, disciplina: Disciplina):
        self.disciplinas.append(disciplina)
        self.notas_por_disciplina.setdefault(disciplina.nome, []) # Metodo de um dicionário que seta um padrão inicial para um dicionário, (chave e valor inicial). 

    def adicionar_nota(self, disciplina: Disciplina, nota: float):
        self.notas_por_disciplina[disciplina.nome].append(nota)

    def calcular_media_d(self, d:Disciplina) -> float:
        notas = self.notas_por_disciplina.get(d.nome, [])
        if not notas:
            return 0
        return sum(notas) / len(notas)

    def calcular_media_geral(self) -> float:
        medias = []
        for d in self.disciplinas:
            media_d = self.calcular_media_d(d)
            medias.append(media_d)

        if not medias:
            return 0
        return sum(medias) / len(medias)