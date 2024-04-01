if __name__ == "__main__": # Función Main para iniciar el código
    
    # Se declaran las variables
    num_anter: int
    factorial: int
    number = int(input("Ingrese un número")) # Se pide ingresar un valor para la variable

    # Para el caso especial de 0 se hace un if, ya que no cumple con la formula
    if number == 0: 
        print("Su factorial es 1")

    # En cualquier otro natural que no sea 0 se sigue el algoritmo
    else:
        # Se inician las variables para el ciclo
        number += 1
        num_anter = 1

        # El ciclo termina en 2 ya que multiplicar por 1 resulta en el mismo valor
        while(number > 1 ):

            # Se actualiza la variable para que en la proxima iteración tome el valor menor a este
            number -= 1

            # Se multiplica el numero actual por el anterior y se va "acumulando" la factorización
            factorial = number * num_anter 
            
            # Se iguala el num anterior a la factorización para que en la próxima iteración se siga acumulando
            num_anter = factorial

        print("Su factorial es:", str(factorial)) # Se muestra el valor del factorial del número ingresado