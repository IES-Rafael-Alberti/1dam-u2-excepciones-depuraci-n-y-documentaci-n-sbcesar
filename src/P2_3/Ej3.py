def cuentaRegresiva(num):
    """
    Imprime una cuenta regresiva desde 'num' hasta 0.

    Args:
        num (int): El número desde el cual vamos imprimiendo los números hasta llegar a 0.

    Raises:
        ValueError: Salta un error indicando que solo se pueden introducir números positivos.

    Returns:
        int: Devuelve el último número impreso que debe ser 0.
    """
    if num <= 0:
        raise ValueError("*** Error - No puedes introducir un num negativo ***")
    for i in range(num, -1, -1):
        if i == 0:
            print(i)
        else:
            print(i, end=", ")
    return i

def main():
    """
    Función principal para solicitar un número al usuario y llamar a la función 'cuentaRegresiva'.
    """
    while True:
        try:
            num = int(input("introduce un numero entero positivo: "))
            cuentaRegresiva(num)
        except ValueError as e:
            print(e)
        else:
            if num > 0:
                break

if __name__ == "__main__":
    main()