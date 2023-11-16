def pedirNum(num):
    """
    Imprime una cadena de números impares separados por comas.

    Parámetros:
        num (int): El número hasta el cual imprimimos los números.

    Raises:
        ValueError: Salta un error indicando que solo se pueden introducir números positivos.

    Devuelve:
        int: El último número impar ya sea el tuyo o el anterior.
    """
    if num <= 0:
        raise ValueError("*** Error - El ejercicio te pide introducir solo numeros positivos ***")
    
    for i in range(1, num+1, 2):
        if i == num:
            print(i)
        else:
            print(i, end=", ")
    return i

def main():
    """
    Función principal para solicitar un número al usuario y llamar a la función 'pedirNum'.
    """
    num = int(input("Introduce un numero entero positivo: "))
    try:
        pedirNum(num)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()