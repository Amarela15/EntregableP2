def constructor(names, goals, goals_avoided, assists):
    estadisticas = tuple(zip(goals, goals_avoided, assists))
    nombres = names.split(", ")
    diccionario = dict(zip(nombres, estadisticas))
    return diccionario