def convierteAEntero(entrada):
    """
    Convierte la entrada (str) introducida por el usuario a un número (int) a la fuerza y luego la imprime.

    Args:
        entrada (str): El número que debemos introducir convertido en string para poder 
        controlarlo luego en la excepción.

    Returns:
        str: Devuelve la entrada introducida
    """
    num = int(entrada)
    return num

def main():
    """
    Función principal para solicitar una entrada al usuario y llamar a la función 'convierteAEntero'.
    """
    entrada = input("Introduce un numero entero: ")
    
    try:
        num = convierteAEntero(entrada)
        print("Este es tu número: ", num)
    except Exception as e:
        print("***  Error - Solo admite numeros enteros ***")

if __name__ == "__main__":
    main()