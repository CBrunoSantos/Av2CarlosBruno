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

# Função para gerar o comando SQL de INNER JOIN entre as tabelas GAMES, VIDEOGAMES e COMPANY
def generate_inner_join_sql():
    return """
        SELECT GAMES.title, GAMES.genre, GAMES.release_date, COMPANY.name AS company_name
        FROM GAMES
        INNER JOIN VIDEOGAMES ON GAMES.id_console = VIDEOGAMES.id_console
        INNER JOIN COMPANY ON VIDEOGAMES.id_company = COMPANY.id_company
    """

# Função para executar uma consulta SQL e exibir os resultados
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

# Exemplo de uso
if __name__ == "__main__":
    # Conectando ao banco de dados
    connection = connect_to_database()

    if connection:
        # Gerando o comando SQL de INNER JOIN
        sql_query = generate_inner_join_sql()

        # Executando a consulta SQL
        print("Resultados da consulta:")
        execute_sql_query(connection, sql_query)

        # Fechando a conexão com o banco de dados
        connection.close()
