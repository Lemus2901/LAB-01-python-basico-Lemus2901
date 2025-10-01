"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    suma = 0
    with open("data.csv", "r") as file:
        for line in file:
            # Quitar saltos de línea y separar por tabulador
            columnas = line.strip().split("\t")
            
            # Tomar el valor de la segunda columna (índice 1) y sumarlo
            suma += int(columnas[1])
    return suma
