def validatePassword(password):
    """
    Función que verifica si la contraseña introducida por el usuario es correcta.

    Args:
        password (str): La contraseña introducida por el usuario.
        validPassword (str): La contraseña correcta.

    Raises:
        NameError: Salta el error cuando la contraseña no es la correcta.

    Returns:
        str: Devuelve un mensaje para saber si es correcta la contraseña.
    """
    validPassword = "usuario"

    if password != validPassword:
        raise NameError("Incorrect Password!")
    else:
        return "Correct Password!"

def main():
    """
    Función principal que pide una contraseña y llama a la función 'validatePassword'.
    """
    try:
        password = input("Introduce la contraseña: ")
        print(validatePassword(password))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()