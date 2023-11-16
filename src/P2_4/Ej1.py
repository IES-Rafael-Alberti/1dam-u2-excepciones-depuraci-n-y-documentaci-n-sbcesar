def obtenerListaOrdenada(num):
    num = int(num)
    return [num]

def ordenarLista(lista):
    total = len(lista)
    posicion = 0
    x = 0
    for i in range(0, len(lista)):
        for j in range(0, total - 1):
            if lista[posicion] > lista[posicion+1]:
                x = lista[posicion]
                lista[posicion], lista[posicion + 1] = lista[posicion + 1], x
                x = 0
            posicion += 1
        posicion = 0
        total -= 1
    return lista

def main():
    lista = []
    while True:
        num = input("Introduce numeros enteros para ordenarlos: ")
        if num == "":
            break
        lista += obtenerListaOrdenada(num)

    print("Lista original: ", lista)
    print("Lista ordenada: ", ordenarLista(lista))

    """
    Lo que puso Diego
    listaOrdenada = ordenarLista(num)
    print(obtenerListaOrdenada(ordenarLista(num)))
    """

if __name__ == "__main__":
    main()