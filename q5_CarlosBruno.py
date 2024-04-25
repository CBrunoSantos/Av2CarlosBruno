from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from passlib.hash import pbkdf2_sha256

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
    password_hash = Column(String)

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

# Inicializando o Flask
app = Flask(__name__)

# Rota para criar um novo usuário
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    name = data['name']
    country = data['country']
    password = data['password']
    password_hash = pbkdf2_sha256.hash(password)
    
    # Salvar usuário no banco de dados
    new_user = User(name=name, country=country, password_hash=password_hash)
    session.add(new_user)
    session.commit()

    return jsonify({"message": "User created successfully"}), 201

# Rota para autenticar o usuário
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['name']
    password = data['password']

    # Buscar usuário no banco de dados
    user = session.query(User).filter_by(name=username).first()

    if user:
        # Verificar a senha
        if pbkdf2_sha256.verify(password, user.password_hash):
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Invalid username or password"}), 401
    else:
        return jsonify({"message": "Invalid username or password"}), 401

if __name__ == '__main__':
    app.run(debug=True)
