def generate_inner_join():
    return """
    SELECT GAMES.title, GAMES.release_date, COMPANY.name AS company_name
    FROM GAMES
    INNER JOIN VIDEOGAMES ON GAMES.id_console = VIDEOGAMES.id_console
    INNER JOIN COMPANY ON VIDEOGAMES.id_company = COMPANY.id_company
    """

def generate_select_query(attributes):
    return """
    SELECT {}
    FROM GAMES
    INNER JOIN VIDEOGAMES ON GAMES.id_console = VIDEOGAMES.id_console
    INNER JOIN COMPANY ON VIDEOGAMES.id_company = COMPANY.id_company
    """.format(", ".join(attributes))

# Exemplo de uso:
if __name__ == "__main__":
    # Gerar INNER JOIN
    inner_join_query = generate_inner_join()
    print("INNER JOIN query:")
    print(inner_join_query)

    # Gerar SELECT query com atributos específicos
    attributes = ['GAMES.title', 'GAMES.release_date', 'COMPANY.name AS company_name']
    select_query = generate_select_query(attributes)
    print("\nSELECT query with specific attributes:")
    print(select_query)
