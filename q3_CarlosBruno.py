from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Criando a conexão com o banco de dados (substitua 'sqlite:///database.db' com o seu tipo e local do banco de dados)
engine = create_engine('sqlite:///database.db', echo=True)

# Declarando a base do modelo
Base = declarative_base()

# Definindo a classe da tabela USERS
class User(Base):
    __tablename__ = 'USERS'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)
    id_console = Column(Integer, ForeignKey('VIDEOGAMES.id_console'))

    videogames = relationship('Videogame', back_populates='users')

# Definindo a classe da tabela VIDEOGAMES
class Videogame(Base):
    __tablename__ = 'VIDEOGAMES'

    id_console = Column(Integer, primary_key=True)
    name = Column(String)
    id_company = Column(Integer, ForeignKey('COMPANY.id_company'))
    release_date = Column(Date)

    company = relationship('Company', back_populates='videogames')
    games = relationship('Game', back_populates='videogame')
    users = relationship('User', back_populates='videogames')

# Definindo a classe da tabela GAMES
class Game(Base):
    __tablename__ = 'GAMES'

    id_game = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)
    release_date = Column(Date)
    id_console = Column(Integer, ForeignKey('VIDEOGAMES.id_console'))

    videogame = relationship('Videogame', back_populates='games')

# Definindo a classe da tabela COMPANY
class Company(Base):
    __tablename__ = 'COMPANY'

    id_company = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)

    videogames = relationship('Videogame', back_populates='company')

# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)
