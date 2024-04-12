def goleador (diccionario):
    max_goles= max(diccionario.items(), key = lambda x: x[1][0])
    return max_goles

def mas_influyente(diccionario):
    def ponderado (items):
        return items[0] * 1.5 + items[1] * 1.25 + items[2]
    max_influyente = max(diccionario.items(), key=lambda x: ponderado(x[1]))
    total = ponderado(max_influyente[1])
    return max_influyente, total