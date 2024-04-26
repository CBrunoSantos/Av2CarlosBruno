import mysql.connector

# Conexão ao Banco de Dados
connect_to_database = lambda: mysql.connector.connect(
    host='localhost',
    user='root',
    password='Br041100!',
    database="bancopython"
) or None

# Função para criar as tabelas no banco de dados, se ainda não existirem
create_tables = lambda connection: (
    (lambda cursor: (
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS USERS (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                country VARCHAR(255),
                id_console INT
            )
        """),

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS VIDEOGAMES (
                id_console INT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                id_company INT,
                release_date DATE
            )
        """),

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS GAMES (
                id_game INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                genre VARCHAR(255),
                release_date DATE,
                id_console INT
            )
        """),

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS COMPANY (
                id_company INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                country VARCHAR(255)
            )
        """),

        connection.commit(),
        print("Tabelas criadas com sucesso.")
    ))(connection.cursor())
) or print("Erro ao criar tabelas.")

# Função para inserir um novo usuário na tabela USERS
insert_user = lambda connection, name, country, id_console: (
    (lambda cursor: (
        cursor.execute("INSERT INTO USERS (name, country, id_console) VALUES (%s, %s, %s)", (name, country, id_console)),
        connection.commit(),
        print("Usuário inserido com sucesso.")
    ))(connection.cursor())
) or print("Erro ao inserir usuário.")

# Função para remover um usuário da tabela USERS
remove_user = lambda connection, user_id: (
    (lambda cursor: (
        cursor.execute("DELETE FROM USERS WHERE id = %s", (user_id,)),
        connection.commit(),
        print("Usuário removido com sucesso.")
    ))(connection.cursor())
) or print("Erro ao remover usuário.")

# Função para consultar todos os registros de uma tabela
query_table = lambda connection, table_name: (
    (lambda cursor: (
        cursor.execute(f"SELECT * FROM {table_name}"),
        records := cursor.fetchall(),
        [
            print(record) for record in records
        ] if records else print("Nenhum registro encontrado.")
    ))(connection.cursor())
) or print(f"Erro ao consultar registros.")

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
