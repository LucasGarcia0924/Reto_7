if __name__ == "__main__": # Función Main para iniciar el código

    # Se declaran las variables
    n = int
    modulo = int
    dato = int(input("Ingresa un valor entre 2 y 50")) # Se ingresa el valor pedido

    # Para el caso en donde se ingrese un valor dentro del intervalo especificado
    if dato > 1 and dato < 51:

        print("El número:", str(dato), "tiene como divisores a:") # Se muestra un "título" para la lista

        # Se inicia la variable para el ciclo
        n = 1
        while (n <= dato): # El ciclo se repite hasta que n sea mayor que el valor dado
            modulo = dato % n

            # Si el módulo es igual a 0 significa que es un divisor y por ende se imprime
            if modulo == 0:
                print(str(n))
            n += 1 # se suma 1 al valor de n para que se sigan obteniendo los divisores dentro del ciclo
    
    # Para el caso en donde se ingrese un valor fuera del intervalo especificado
    else:
        print("No es un número que esté en el intervalo que te pedí")