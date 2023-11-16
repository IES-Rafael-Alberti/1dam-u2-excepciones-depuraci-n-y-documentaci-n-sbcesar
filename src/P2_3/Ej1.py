def imprimirEdad(edad):
    """
    Imprime números del 1 hasta la 'edad' proporcionada.

    Parámetros:
        edad (int): La edad hasta la cual imprimir números.

    Devuelve:
        int: El último número impreso.

    Ejemplo de uso:
        >>> imprimirEdad(5)
        1 2 3 4 5
        5
    """
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    
    for i in range(1, edad+1):
        print(i, end=" ")
    return i

def main():
    """
    Función principal para solicitar la edad al usuario y llamar a imprimirEdad.

    Esta función solicita al usuario que introduzca su edad, luego llama a la función imprimirEdad
    pasando la edad como argumento. Captura cualquier ValueError que pueda surgir e imprime un mensaje
    de error en ese caso.

    Ejemplo de uso:
        >>> main()
        Introduce tu edad: 3
        1 2 3
    """
    edad = int(input("Introduce tu edad: "))
    try:
        imprimirEdad(edad)
    except ValueError as e:
        print("Error " + str(e))

if __name__ == "__main__":
    main()