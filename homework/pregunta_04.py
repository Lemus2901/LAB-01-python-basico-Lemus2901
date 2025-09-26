def pregunta_04():
    conteo = {}
    with open("data.csv", "r") as file:
        for line in file:
            columnas = line.strip().split("\t")
            fecha = columnas[2]
            
            # extraer mes (MM)
            mes = fecha.split("-")[1]
            
            # contar
            if mes in conteo:
                conteo[mes] += 1
            else:
                conteo[mes] = 1
    
    # ordenar por mes y devolver lista de tuplas
    resultado = sorted(conteo.items())
    
    return resultado
