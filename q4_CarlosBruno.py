import mysql.connector

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

def generate_inner_join_sql():
    return """
        SELECT GAMES.title, GAMES.genre, GAMES.release_date, COMPANY.name AS company_name
        FROM GAMES
        INNER JOIN VIDEOGAMES ON GAMES.id_console = VIDEOGAMES.id_console
        INNER JOIN COMPANY ON VIDEOGAMES.id_company = COMPANY.id_company
    """

def execute_sql_query(connection, sql_query):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_query)
        records = cursor.fetchall()
        if records:
            for record in records:
                print(record)
        else:
            print("Nenhum registro encontrado.")
    except mysql.connector.Error as error:
        print(f"Erro ao executar consulta SQL: {error}")

if __name__ == "__main__":
    connection = connect_to_database()

    if connection:
        sql_query = generate_inner_join_sql()

        print("Resultados da consulta:")
        execute_sql_query(connection, sql_query)

        connection.close()
