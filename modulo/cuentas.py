def goleador (diccionario):
    max_goles= max(diccionario.items(), key = lambda x: x[1][0])
    return max_goles