#Inicialización tablero y mostrar tablero


def inicializaTablero():
    """ 
    InicializaTablero:: None -> List 
    Inicializa el tablero. Cada lista dentro de tablero representa una fila, y cada item dentro de dichas filas representa una casilla correspondiente.
    """
    i = 0 #iterador
    tablero = []
    fila = ['' for x in range(8)]

    while i < 8:
        tablero += [fila]
        i += 1

    return tablero


def mostrarTablero():
    pass