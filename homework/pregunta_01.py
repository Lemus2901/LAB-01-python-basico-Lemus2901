"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    total = 0
    with open("data.csv", "r") as file:
        for line in file:
            # quitar salto de línea y separar por tabulador
            columnas = line.strip().split("\t")
            
            # tomar la segunda columna (índice 1)
            valor = int(columnas[1])
            
            # acumular
            total += valor
    
    return total

