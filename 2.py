if __name__ == "__main__": # Función Main para iniciar el código
    
    i: int # Declaro la variable

    print("Números impares:") # Señalización o título de la lista
    
    # Inicio la variable para el ciclo
    i = 0 
    while(i <= 999) : # El ciclo se repite para todo i menor o igual a 999

        i += 1 # Se actualiza la variable para que tome el siguiente valor
        if (i % 2) == 0: # Si el módulo de i y 2 es igual a 0, osea es par, continua y no escribe dicho i
            continue
        print(str(i)) # Muestra al usuario la lista

    print("Números pares:") # Señalización o titulo de la lista

    # inicio la variable para el ciclo
    i = 0
    while(i <= 999) : # El ciclo se repite para todo i menor o igual a 999

        i += 1 # Se actualiza la variable para que tome el siguiente valor
        if (i % 2) != 0: # Si el módulo de i y 2 es diferente a 0, osea es impar, continua y no escribe dicho i
            continue
        print(str(i)) # Muestra al usuario la lista