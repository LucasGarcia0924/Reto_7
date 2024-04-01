if __name__ == "__main__": # Función Main para iniciar el código

    # Se declaran las variables
    poblacion_A:float
    poblacion_B:float
    crecimiento_A:float
    crecimiento_B: float
    year:int

    # Se inicializan las variables para el ciclo
    poblacion_A = 25
    poblacion_B = 18.9
    year = 2022

    # El ciclo se repite hasta que la población del país B sea mayor a la del país A
    while(poblacion_A >= poblacion_B):
        
        # Se calcula el crecimiento de cada población
        crecimiento_A = poblacion_A * 0.02
        crecimiento_B = poblacion_B * 0.03
        
        # Se actualizan las variables con el crecimiento
        poblacion_A += crecimiento_A
        poblacion_B += crecimiento_B
        year += 1 # Se aumenta en 1 el año transcurrido
        
    # Se muestra el año en donde la población del país B supera a la del país A
    print("La población del país B superó a la del país A, en el año", str(year))