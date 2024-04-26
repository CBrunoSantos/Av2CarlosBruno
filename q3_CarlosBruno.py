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

# Função para remover um usuário da tabela USERS
def remove_user(connection, user_id):
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM USERS WHERE id = %s"
        cursor.execute(sql, (user_id,))
        connection.commit()
        print("Usuário removido com sucesso.")
    except mysql.connector.Error as error:
        print(f"Erro ao remover usuário: {error}")

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

        # Inserindo um novo usuário
        insert_user(connection, "Alice", "USA", 1)

        # Consultando a tabela USERS
        print("Registros na tabela USERS:")
        query_table(connection, "USERS")

        # Removendo o usuário com id = 1
        remove_user(connection, 1)

        # Consultando novamente a tabela USERS após a remoção
        print("Registros na tabela USERS após remoção:")
        query_table(connection, "USERS")

        # Fechando a conexão com o banco de dados
        connection.close()
