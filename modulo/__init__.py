def constructor(names, goals, goals_avoided, assists):
    """
    Construye un diccionario a partir de los nombres de los jugadores y sus estadísticas de rendimiento.

    Parameters:
    names (str): Una cadena que contiene los nombres de los jugadores separados por comas.
    goals (list): Una lista que contiene la cantidad de goles anotados por cada jugador.
    goals_avoided (list): Una lista que contiene la cantidad de goles evitados por cada jugador.
    assists (list): Una lista que contiene la cantidad de asistencias realizadas por cada jugador.

    Returns:
    dict: Un diccionario que mapea el nombre de cada jugador a una tupla de sus estadísticas de rendimiento, donde el primer elemento de la tupla representa la cantidad de goles, 
    el segundo elemento representa la cantidad de goles evitados y el tercer elemento representa la cantidad de asistencias.
    """
    estadisticas = tuple(zip(goals, goals_avoided, assists))
    nombres = names.split(", ")
    diccionario = dict(zip(nombres, estadisticas))
    return diccionario