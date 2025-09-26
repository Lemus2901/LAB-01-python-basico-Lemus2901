"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    conteo = {}
    with open("data.csv", "r") as file:
        for line in file:
            columnas = line.strip().split("\t")
            letra = columnas[0]
            
            # contar la letra
            if letra in conteo:
                conteo[letra] += 1
            else:
                conteo[letra] = 1
    
    # ordenar alfabéticamente y convertir a lista de tuplas
    resultado = sorted(conteo.items())
    
    return resultado
