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
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    ra = Column("ra", Integer)
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

os.system('cls || clear')

print("\nListando alunos no banco de dados")
lista_alunos = session.query(Aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.id} - {aluno.ra} - {aluno.nome} - {aluno.idade} - {aluno.senha}")

print("\nExcluindo alunos no banco de dados")
ra_aluno = input("Informe o R.A do aluno: ")
aluno = session.query(Aluno).filter_by(ra=ra_aluno).first()
if aluno:
    session.delete(aluno)
    session.commit()
    print("\nUsuário deletado com sucesso!")
else:
    print("\nUsuário não encontrado!")

# usuario = Usuario("Ruan", "Ruan@gmail.com", "123")
# aluno = Aluno(ra=222, nome="Ruan", idade=22, senha="123")
# session.add(aluno)
# session.commit()

# Mostrando conteúdo do banco de dados.
# SELECT * FROM Usuarios
print("\nListando usuários do banco de dados")
lista_alunos = session.query(Aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.id} - {aluno.ra} - {aluno.nome}  - {aluno.idade} - {aluno.senha}")

# Atualizar um aluno.
print("\nAtualizando os dados de um usuário.")

ra_aluno = input("Informe o R.A. do aluno: ")

aluno = session.query(Aluno).filter_by(ra=ra_aluno).first()

if aluno:
    aluno.ra = input("Digite o seu R.A.: ")
    aluno.nome = input("Digite o seu nome: ")
    aluno.idade = input("Digite a sua idade: ")
    aluno.senha = input("Digite a sua senha: ")
    session.commit()
else:
    print("Usuário não encontrado!")

# Pesquisando um usuário
print("\nPesquisando um usuário pelo R.A. .")

ra_aluno = input("Informe o R.A. do aluno: ")

aluno = session.query(Aluno).filter_by(ra=ra_aluno).first()

if aluno:
    print(f"{aluno.id} - {aluno.ra} - {aluno.nome}  - {aluno.idade} - {aluno.senha}")
else:
    print("Usuário não encontrado!")

#Fechando conexão.
session.close()