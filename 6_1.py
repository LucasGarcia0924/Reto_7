import random # Se importa el modulo para usarlo posteriormente

if __name__ == "__main__": # Función Main para iniciar el código

    # Se declaran las variables
    lim_inf: int
    lim_sup: int
    num_secret: int

    # Se inician las variables para el ciclo
    num_secret = random.randint(1,100) # Se genera el número aleatorio que se ha de adivinar
    acierto = False
    while (acierto == False): # El ciclo se repite hasta que la persona adivine el número
            
        intento = int(input("Intenta adivinar el número")) # Se ingresa el valor que el usuario crea posible

        # Para el caso en donde el número no siga las indicaciones y este fuera del intevalo
        if intento > 100 or intento < 1: 
            print("Es un número entre 1 y 100")
            continue
            
        # Para cuando finalmente se adivine el número y se termine el ciclo
        elif intento == num_secret:
            print("Lo lograste, acertaste!")
            acierto = True # Se actualiza la variable para poner fin al ciclo
                
        # Para cuando el número dado sea mayor al número por adivinar
        elif intento > num_secret:
            print("Te pasaste, es menor a ese")
            
        # Si ninguno de los anteriores se cumple se da el caso de que el número dado es menor al número por adivinar
        else:
            print("No, el número es mayor a este")