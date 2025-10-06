class Pessoa:
    def __init__(self,nome,documento,matricula):
        self.nome = nome
        self.documento = documento
        self.matricula = matricula
    def __str___(self):
        return f"{self.nome} matricula;{self.metricula} documento: {self.documento}"

    def __eq__(self, other):
        return self.documento == other.documento
    def __hash__(self):
        return hash(self.documento)
class aluno(Pessoa):
    def __init__(self,nome,documento,matricula):
        super().__init__(nome,documento,matricula)
        def __str__(self):
            return f"aluno: {self.nome} matricula: {self.matricula} documento: {self.documento}"
class professor(Pessoa):
    def __init__(self,nome,documento,materia):
        super().__init__(nome,documento,materia)
        self.materia = materia
        def __str__(self):
            return f"professor: {self.nome} materia:{self.materia} Documento: {self.documento}"
class curso:
    def __init__(self,nome,codigo):
        self.nome = nome
        self.codigo = codigo
        self.alunos = set()
        self.professores = set()
    def adicionar_aluno(self,aluno):
        self.alunos.add(aluno)
    def adicionar_professor(self,professor):
        self.professores.add(professor)
class sistema:
    def __init__(self):
        self.alunos = set()
        self.professores = set()
        self.cursos = set()
    def cadastrar_aluno(self,aluno):
        self.alunos.add(aluno)
    def cadastrar_professor(self,professor):
        self.professores.add(professor)
    def cadastrar_curso(self,curso):
        self.cursos.add(curso)
    def listar_alunos(self):
        print("\n Alunos")
        for aluno in self.alunos:
            print(aluno)
    def listar_professores(self):
        print("\n professores")
        for professores in self.professores:
            print(professores)
    def listar_cursos(self):
        print("\n Cursos")
        for cursos in self.cursos:
            print(cursos)

if __name__ == "__main__":
    sistema = sistema()
    a1 = aluno("Eduardo","12345","54321")
    a2 = aluno("Junio","98765","56789")
    p1 = professor("José","987654321","Educação fisica")
    p2 = professor("Eduardo","123456789","Matematica")
    c1 = curso("Desenvolvedor Back-End","DBE101")

sistema.cadastrar_aluno(a1)
sistema.cadastrar_aluno(a2)
sistema.cadastrar_professor(p1)
sistema.cadastrar_professor(p2)
sistema.cadastrar_curso(c1)
c1.adicionar_aluno(a1)
c1.adicionar_professor(p1)
sistema.listar_alunos()
sistema.listar_professores()
sistema.listar_cursos()
print("\n detalhes do curso")
print(c1)
print("alunos inscritos:")
for aluno in c1.alunos:
    print(f" {aluno}")
print("professores responsaveis")
for prof in c1.professores:
    print(f"{prof}")