if __name__ == "__main__": # Función Main para iniciar el código
    
    num = int(input("Digita un número")) # Se pide ingresar el valor de la variable

    # Se inicializa la variable para el ciclo
    num += 1
    while(num >= 2): # El ciclo se repite para todo num hasta llegar a ser igual a 2

        num -= 1 # Se actualiza la variable para que en la proxima iteración tome el valor menor a este
        if (num % 2) != 0: # Si el num es impar el ciclo continua pero omite la iteración actual
            continue
        print(num) # Se muestra el num en la terminal