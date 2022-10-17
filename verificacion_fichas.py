#Todo lo relacionado a la verificación de coordenadas y jugadas

def verificacionFormato(coordenada):
    """
    verificacionFormato :: string -> bool

    La función toma un strin no vacío leído del archivo de juego y 
    nos determina si tiene como primer valor un string y un número
    como segundo. También verifica que dicho string, tenga exactamente
    una longitud de dos.
    """

    if len(coordenada) != 2:
        print("Las coordenadas solo deben tener dos componentes.")
        return False
    
    columna, fila = coordenada[0],coordenada[1]
        
    if not columna.isalpha():
        print("Las columnas deben ser representada con letras.")
        return False

    if not fila.isdigit():
        print("Las filas deben ser representadas con números.")
        return False

    return True


def verificacionRango(coordenada):
    """
    verificacionRango :: string -> bool

    Dado un string no vacío, nos determina si dicha coordenada
    se encuentra dentro de los límites del tablero.
    """
    
    if not verificacionFormato(coordenada):
        return False

    columnas = ['A','B','C','D','E','F','G','H']

    columna = coordenada[0].upper()
    fila = int(coordenada[1])

    return (columna in columnas) and (1 <= fila <= 8)



def convertirCoordenada(coordenada):
    """
    convertirCoordenada :: str -> (int,int)

    Dada una coordenada válida leida del archivo, la convertimos en la
    coordenada equivalente con la que trabajaremos:
    - A las letras de la A a la H, las relacionamos con los números
      del 0 al 7.
    - A los números del 1 al 8, los relacionamos con los números del
      0 al 7.
    """
    
    columnas = ['A','B','C','D','E','F','G','H']

    columna = coordenada[0].upper()
    fila = int(coordenada[1])

    columnaEquivalente = columnas.index(columna)
    filaEquivalente = fila - 1

    return columnaEquivalente,filaEquivalente





def fichasVolteadas(tablero,coordenada):
    """
    fichasVolteadas :: list(list(str) str -> list(tuple(int))

    Dado el tablero actual y una coordenada, nos devuelve una lista de
    tuplas
    """
    pass
