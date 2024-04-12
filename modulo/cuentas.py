def goleador (diccionario):
    """
    Devuelve el jugador/a con la mayor cantidad de goles.

    Parameters:
    diccionario (dict): Un diccionario que mapea el nombre del jugador/a a una tupla de estadísticas de rendimiento, donde el primer elemento de la tupla representa la cantidad de goles.

    Returns:
    tuple: Una tupla que contiene el nombre del jugador/a y su cantidad de goles.
    """
    max_goles= max(diccionario.items(), key = lambda x: x[1][0])
    return max_goles

def mas_influyente(diccionario):
    """
    Devuelve el jugador/a más influyente en función de una ponderación específica de sus estadísticas.
    
    Parameters:
    diccionario (dict): Un diccionario que mapea el nombre del jugador/a a una tupla de estadísticas de rendimiento.

    Returns:
    tuple: Una tupla que contiene el nombre del jugador/a más influyente y su puntaje total ponderado.
    """
    def ponderado (items):
        return items[0] * 1.5 + items[1] * 1.25 + items[2]
    max_influyente = max(diccionario.items(), key=lambda x: ponderado(x[1]))
    total = ponderado(max_influyente[1])
    return max_influyente, total

#def promedio_equipo(diccionario):
#    suma = sum(valor[0] for valor in diccionario.values())
#    return suma / 25
def promedio_equipo(goles):
    """
    Calcula el promedio de goles por partido para todo el equipo.

    Parameters:
    goles (list): Una lista que contiene la cantidad de goles anotados por el equipo en cada uno de los 25 partidos.

    Returns:
    float: El promedio de goles por partido para todo el equipo.
    """
    return sum(goles) / 25

def promedio_goleador(top_scorer):
    """
    Calcula el promedio de goles por partido para el jugador/a con más goles.

    Parameters:
    top_scorer (tuple): Una tupla que contiene el nombre del jugador/a y su tupla de estadísticas de rendimiento, donde el primer elemento de la tupla representa la cantidad de goles.

    Returns:
    float: El promedio de goles por partido para el jugador/a con más goles.
    """
    return top_scorer[1][0] / 25
    