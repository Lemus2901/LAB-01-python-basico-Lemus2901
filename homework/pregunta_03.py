"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    sumas = {}
    with open("data.csv", "r") as file:
        for line in file:
            columnas = line.strip().split("\t")
            letra = columnas[0]
            valor = int(columnas[1])
            
            # acumular la suma
            if letra in sumas:
                sumas[letra] += valor
            else:
                sumas[letra] = valor
    
    # ordenar por letra y convertir a lista de tuplas
    resultado = sorted(sumas.items())
    
    return resultado
