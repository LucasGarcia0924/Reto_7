import random # Se importa el modulo para usarlo posteriormente

if __name__ == "__main__": # Función Main para iniciar el código

    # Se muestran las instrucciones básicas
    print("Piensa en un número, trataré de adivinarlo")
    print("Por favor responde a cada pregunta con \"Si\" o \"No\"")

    # Se declaran las variables
    lim_inf: int
    lim_sup: int
    suposicion: int

    # Se inician las variables para el ciclo
    lim_inf = 1
    lim_sup = 100
    suposicion = random.randint(lim_inf,lim_sup)
    acierto = False

    # El ciclo se repite hasta que la adivinanza haya acertado
    while (acierto == False):
        
        # Pregunta si tu número es mayor a uno que se genera al azar con los límites dados
        print("¿Tu número es mayor a:", str(suposicion), "?") 
        respuesta = str(input())
        match respuesta:
            case "Si":
                lim_inf = suposicion # actualiza el límite inferior
            case "No":
                lim_sup = suposicion # actualiza el límite superior

            # En caso de digitar un valor incorrecto se despliega el sgte mensaje
            case _:
                print("Respuesta inválida")
        suposicion = random.randint(lim_inf,lim_sup) # Se crea otra suposición con los nuevos límites

        # Pregunta si tu número es menor a uno que se genera al azar con los límites dados
        print("¿Tu número es menor a:", str(suposicion), "?")
        respuesta = str(input())
        match respuesta:
            case "Si":
                lim_sup = suposicion # actualiza el límite superior
            case "No":
                lim_inf = suposicion # actualiza el límite inferior
            
            # En caso de digitar un valor incorrecto se despliega el sgte mensaje
            case _:
                print("Respuesta inválida")
        suposicion = random.randint(lim_inf,lim_sup) # Se crea otra suposición con los nuevos límites

        # Pregunta si tu número es igual a uno que se genera al azar con los límites dados
        print("¿Tu número es igual a:", str(suposicion), "?")
        respuesta = str(input())

        # Si se da el caso de que sean iguales, se actualiza la variable y se termina el ciclo
        if respuesta == "Si":
            acierto = True 

        # Se crea otra suposición con los nuevos límites por si no se ha terminado el ciclo
        suposicion = random.randint(lim_inf,lim_sup)
            
    print("Ja!, lo logré, tu número es:", str(suposicion)) # Celebración de la máquina