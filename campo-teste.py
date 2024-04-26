import mysql.connector

# Conexão ao Banco de Dados
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Br041100!',
            database="bancopython"
        )
        print("Conexão ao banco de dados bem-sucedida.")
        return connection
    except mysql.connector.Error as error:
        print(f"Erro ao conectar ao banco de dados: {error}")
        return None

# Função para criar as tabelas no banco de dados, se ainda não existirem
def create_tables(connection):
    try:
        cursor = connection.cursor()

        # Criação da tabela USERS
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS USERS (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                country VARCHAR(255),
                id_console INT
            )
        """)

        # Criação da tabela VIDEOGAMES
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS VIDEOGAMES (
                id_console INT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                id_company INT,
                release_date DATE
            )
        """)

        # Criação da tabela GAMES
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS GAMES (
                id_game INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                genre VARCHAR(255),
                release_date DATE,
                id_console INT
            )
        """)

        # Criação da tabela COMPANY
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS COMPANY (
                id_company INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                country VARCHAR(255)
            )
        """)

        connection.commit()
        print("Tabelas criadas com sucesso.")
    except mysql.connector.Error as error:
        print(f"Erro ao criar tabelas: {error}")

# Função para inserir um novo usuário na tabela USERS
def insert_user(connection, name, country, id_console):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO USERS (name, country, id_console) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, country, id_console))
        connection.commit()
        print("Usuário inserido com sucesso.")
    except mysql.connector.Error as error:
        print(f"Erro ao inserir usuário: {error}")

# Função para inserir um novo videogame na tabela VIDEOGAMES
def insert_videogame(connection, id_console, name, id_company, release_date):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO VIDEOGAMES (id_console, name, id_company, release_date) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (id_console, name, id_company, release_date))
        connection.commit()
        print("Videogame inserido com sucesso.")
    except mysql.connector.Error as error:
        print(f"Erro ao inserir videogame: {error}")

# Função para inserir um novo jogo na tabela GAMES
def insert_game(connection, title, genre, release_date, id_console):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO GAMES (title, genre, release_date, id_console) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (title, genre, release_date, id_console))
        connection.commit()
        print("Jogo inserido com sucesso.")
    except mysql.connector.Error as error:
        print(f"Erro ao inserir jogo: {error}")

# Função para inserir uma nova empresa na tabela COMPANY
def insert_company(connection, name, country):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO COMPANY (name, country) VALUES (%s, %s)"
        cursor.execute(sql, (name, country))
        connection.commit()
        print("Empresa inserida com sucesso.")
    except mysql.connector.Error as error:
        print(f"Erro ao inserir empresa: {error}")

# Função para consultar todos os registros de uma tabela
def query_table(connection, table_name):
    try:
        cursor = connection.cursor()
        sql = f"SELECT * FROM {table_name}"
        cursor.execute(sql)
        records = cursor.fetchall()
        if records:
            for record in records:
                print(record)
        else:
            print("Nenhum registro encontrado.")
    except mysql.connector.Error as error:
        print(f"Erro ao consultar registros: {error}")

# Exemplo de uso
if __name__ == "__main__":
    # Conectando ao banco de dados
    connection = connect_to_database()

    if connection:
        # Criando as tabelas, se ainda não existirem
        create_tables(connection)

        # Inserindo alguns dados de exemplo

        # Inserindo usuários
        insert_user(connection, "Alice", "USA", 1)
        insert_user(connection, "Bob", "UK", 2)
        insert_user(connection, "Carol", "Canada", 1)
        insert_user(connection, "David", "Australia", 3)
        insert_user(connection, "Eve", "Germany", 2)

        # Inserindo videogames
        insert_videogame(connection, 1, "Super Mario Odyssey", 1, "2017-10-27")
        insert_videogame(connection, 2, "The Legend of Zelda: Breath of the Wild", 1, "2017-03-03")
        insert_videogame(connection, 3, "God of War", 2, "2018-04-20")
        insert_videogame(connection, 4, "Red Dead Redemption 2", 3, "2018-10-26")
        insert_videogame(connection, 5, "Cyberpunk 2077", 4, "2020-12-10")

        # Inserindo jogos
        insert_game(connection, "Super Mario Odyssey", "Platformer", "2017-10-27", 1)
        insert_game(connection, "The Legend of Zelda: Breath of the Wild", "Action-adventure", "2017-03-03", 2)
        insert_game(connection, "God of War", "Action-adventure", "2018-04-20", 3)
        insert_game(connection, "Red Dead Redemption 2", "Action-adventure", "2018-10-26", 4)
        insert_game(connection, "Cyberpunk 2077", "Action RPG", "2020-12-10", 5)

        # Inserindo empresas
        insert_company(connection, "Nintendo", "Japan")
        insert_company(connection, "Sony Interactive Entertainment", "Japan")
        insert_company(connection, "Rockstar Games", "USA")
        insert_company(connection, "CD Projekt", "Poland")

        # Consultando a tabela USERS após inserção
        print("\nRegistros na tabela USERS após inserção:")
        query_table(connection, "USERS")

        # Consultando a tabela VIDEOGAMES após inserção
        print("\nRegistros na tabela VIDEOGAMES após inserção:")
        query_table(connection, "VIDEOGAMES")

        # Consultando a tabela GAMES após inserção
        print("\nRegistros na tabela GAMES após inserção:")
        query_table(connection, "GAMES")

        # Consultando a tabela COMPANY após inserção
        print("\nRegistros na tabela COMPANY após inserção:")
        query_table(connection, "COMPANY")

        # Fechando a conexão com o banco de dados
        connection.close()
