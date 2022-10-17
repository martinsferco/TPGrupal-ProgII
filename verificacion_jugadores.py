#Verificación de información de los jugadores

def verificaDatos(archivo):
    """
    verificaDatos :: file -> bool

    . Recibe el archivo y devuelve true si los colores de ambos no son los mismos y si son B O N, 
      y si el color de inicio es B o N. Sino, devuelve false, indicando que el juego no puede iniciar
    """

    linea = archivo.readline() # linea 1 (jugador 1)

    jugador1 = jugador(linea)

    linea = archivo.readline() # linea 2 (jugador 2)

    jugador2 = jugador(linea)

    linea = archivo.readline() # linea 3 (color que inicia)

    if not coloresCorrectos(jugador1, jugador2): # SI LOS COLORES DE AMBOS SON IGUALES o DIFERENTES DE N Y B, TERMINA
        return False

    if not linea != 'N' and linea != 'B': # SI EL COLOR QUE INICIA ES INCORRECTO, TERMINA
        print('El color que inicia es invalido.')
        return False
    
    return True 


def jugador(linea):
    """
    jugador :: str -> (string, string)

    . Dado un string, lo divide y devuelve una lista [nombre, color]. Luego, avanza una linea en el archivo.
    """

    nombre,color = linea.split(', ')

    return nombre,color[:-1]    

def coloresCorrectos(jugador1, jugador2):
    """
    coloresCorrectos :: (str, str), (str, str) -> bool

    . Si los colores son diferentes, y son N o B, entonces devuelve true, que significa que los colores son 
      validos, sino devuelve false.
    """

    if jugador1[1] != jugador2[1]:
        if jugador1[1] == 'N' or jugador1[1] == 'B':
            if jugador2[1] == 'N' or jugador2[1] == 'B':
                return True

    print('Los colores son incorrectos.')
    return False
