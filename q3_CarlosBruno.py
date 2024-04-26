import mysql.connector

connect_to_database = lambda: mysql.connector.connect(
    host='localhost',
    user='root',
    password='Br041100!',
    database="bancopython"
) or None

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

insert_user = lambda connection, name, country, id_console: (
    (lambda cursor: (
        cursor.execute("INSERT INTO USERS (name, country, id_console) VALUES (%s, %s, %s)", (name, country, id_console)),
        connection.commit(),
        print("Usuário inserido com sucesso.")
    ))(connection.cursor())
) or print("Erro ao inserir usuário.")

remove_user = lambda connection, user_id: (
    (lambda cursor: (
        cursor.execute("DELETE FROM USERS WHERE id = %s", (user_id,)),
        connection.commit(),
        print("Usuário removido com sucesso.")
    ))(connection.cursor())
) or print("Erro ao remover usuário.")

query_table = lambda connection, table_name: (
    (lambda cursor: (
        cursor.execute(f"SELECT * FROM {table_name}"),
        records := cursor.fetchall(),
        [
            print(record) for record in records
        ] if records else print("Nenhum registro encontrado.")
    ))(connection.cursor())
) or print(f"Erro ao consultar registros.")

if __name__ == "__main__":
    connection = connect_to_database()

    if connection:
        create_tables(connection)

        insert_user(connection, "Alice", "USA", 1)

        print("Registros na tabela USERS:")
        query_table(connection, "USERS")

        remove_user(connection, 1)

        print("Registros na tabela USERS após remoção:")
        query_table(connection, "USERS")

        connection.close()
