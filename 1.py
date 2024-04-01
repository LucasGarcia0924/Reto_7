if __name__ == "__main__": # Función Main para iniciar el código
    
    # Declaro variables
    i: int
    cuadrado: int

    # Inicio la variable para el ciclo
    i = 1 
    
    # El ciclo se repite para todo i menor o igual a 100
    while (i<=100):

        cuadrado = i**2 # Se calcula el cuadrado del número
        print(str(i),",",str(cuadrado)) # Se muestra cada número con su cuadrado
        i += 1 # Se actualiza aumentando en 1 el valor de i para que al repetirse el ciclo se tome el valor siguiente

    print("Fin") # Extra para delimitar el fin del código