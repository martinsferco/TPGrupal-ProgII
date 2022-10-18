#Todo lo relacionado a la verificación de coordenadas y jugadas

def verificacionFormato(coordenada):
    """
    verificacionFormato :: string -> bool

    La función toma un string no vacío leído del archivo de juego y 
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


def verificacionOcupada(tablero,coordenada):
    """
    verificacionOcupada :: list(list(str)) str -> bool

    Dado el tablero actual y una coordenada, nos indica si la casilla
    en donde se quiere realizar la jugada se encuentra ocupada o no.
    """
    pass



def fichasVolteadas(tablero,coordenada):
    """
    fichasVolteadas :: list(list(str)) str -> list(tuple(int))

    Dado el tablero actual y una coordenada, nos devuelve una lista de
    tuplas, en donde cada una de las tuplas indica las coordenadas de
    las fichas que se dieron vuelta gracias a la colocación de la ficha
    pasada como argumento.
    En caso de que la lista sea vacía, tenemos cuatro casos:
    - Que la ficha no genéro cambios.
    - Que la ficha no tiene el formato adecuado.
    - Que la ficha no se encentra del rango adecuado.
    - Que la casilla está ocupada.
    En cualquiera de esos casos la lista es vacía, y por lo tanto, la 
    jugada asociada a esa coordenada es incorrecta.
    """
    pass
