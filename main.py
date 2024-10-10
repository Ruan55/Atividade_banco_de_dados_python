import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
db = create_engine("sqlite:///meubanco.db")

# CREATE DATABASE meubanco

# Conexão com o banco de dados.
Session = sessionmaker(bind=db)
session = Session()

# I/0
# I = input (Entrada)
# O = output (Saída)

# Abrindo uma conexão
Base = declarative_base()

# Criando tabela.
class Aluno(Base):
    # Definindo nome da tablea
    __tablename__ = "alunos"

    # Definindo atributos da tabela
    ra = Column("ra", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    senha = Column("senha", String)

    # Definindo atributos da classe
    def __init__(self, ra: int, nome: str, idade: int, senha: str) -> None:
        self.ra = ra
        self.nome = nome
        self.idade = idade
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)

os.system("cls || clear")

# Salvar banco de dados
for i in range(2):
     ra = input("Digite o seu ra: ")
     nome = input("Digite a seu nome: ")
     idade = input("Digite a sua idade: ")
     senha = input("Digite a sua senha: ")

     aluno = Aluno(ra=ra, nome=nome, idade=idade, senha=senha)
     session.add(aluno)
     session.commit()
     print()

print("\nListando alunos no banco de dados")
lista_alunos = session.query(Aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.ra} - {aluno.nome} - {aluno.idade} - {aluno.senha}")

aluno = session.query(Aluno).filter_by(nome="João").first()
session.delete(aluno)
session.commit()
print("\nUsuário deletado com sucesso!")

# usuario = Usuario("Ruan", "Ruan@gmail.com", "123")
# aluno = Aluno(ra=222, nome="Ruan", idade=22, senha="123")
# session.add(aluno)
# session.commit()

# Mostrando conteúdo do banco de dados.
# SELECT * FROM Usuarios
lista_alunos = session.query(Aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.ra} - {aluno.nome}  - {aluno.idade} - {aluno.senha}")