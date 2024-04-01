# Se declaran las funciones a utilizar dentro del codigo
def modulo (valor: int, i: int) -> int: # Se declaran las variables que ingresan y las que salen
    modulando = valor%i
    return modulando # Se devuelve el valor del módulo de las 2 variables

def primo (valor: int, i: int) -> bool: # Se declaran las variables que ingresan y las que salen
    
    # El ciclo se repite hasta que el número sea igual a i
    while(valor > i):
        residuo = modulo(valor,i) # Llama a la funcion "modulo" para obtener dicho valor
        
        if residuo == 0: # Si el módulo es igual a 0 el valor no es primo y se termina el ciclo
            primeidad = False
            break # Rompe el ciclo, evitando la iteracion actual y las siguientes
        i += 1 # Se le aumenta el valor a i en 1 para que se obtenga el módulo próximo
        primeidad = True

    return primeidad # Se devuelve un booleano que indica si el valor es primo o no

if __name__ == "__main__": # Función Main para iniciar el código
    
    # Se declaran las variables
    valor: int
    i: int
    
    print("La lista de números primos del 1 al 100 es:") # Se muestra un "título" para la lista
    print("2") # Se agrega el 2 a la lista pues ya se sabe que es un número primo entre 1 y 100
    
    # Se inician las variables para el ciclo
    valor = 3
    i = 2

    while (valor <= 100): # El ciclo se repite hasta que el valor sea mayor a 100
        
        # Se llama a la funcion "primo" para verificar si el valor es primo o no
        es_primo = primo(valor,i)
        if es_primo == True:
            print(str(valor)) # Si el valor es primo se imprime

        valor += 1 # Se le suma 1 al valor para en la próxima iteración se verifique el número siguiente
        i = 2 # Se actualiza el valor de i al inicial para que en la próxima iteración comience desde 2