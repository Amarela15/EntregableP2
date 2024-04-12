def goleador (diccionario):
    max_goles= max(diccionario.items(), key = lambda x: x[1][0])
    return max_goles

def mas_influyente(diccionario):
    def ponderado (items):
        return items[0] * 1.5 + items[1] * 1.25 + items[2]
    max_influyente = max(diccionario.items(), key=lambda x: ponderado(x[1]))
    total = ponderado(max_influyente[1])
    return max_influyente, total

#def promedio_equipo(diccionario):
#    suma = sum(valor[0] for valor in diccionario.values())
#    return suma / 25
def promedio_equipo(goles):
    return sum(goles) / 25

def promedio_goleador(top_scorer):
    return top_scorer[1][0] / 25
    