def verificacionFormato(coordenada):
    """
    verificacionFormato :: str -> bool

    La función toma un string leído del archivo de juego y 
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
    verificacionRango :: str -> bool

    Dado un string no vacío, nos determina si dicha coordenada
    se encuentra dentro de los límites del tablero.
    """
    
    if not verificacionFormato(coordenada):
        return False

    columnas = ['A','B','C','D','E','F','G','H']

    columna = coordenada[0].upper()
    fila = int(coordenada[1])

    return (columna in columnas) and (1 <= fila <= 8)



def convertirCoordenadas(coordenada):
    """
    convertirCoordenada :: str -> (int,int)

    Dada una coordenada válida leida del archivo, la convertimos en la
    coordenada equivalente con la que trabajaremos:
    - A las letras de la A a la H, las relacionamos con los números
      del 0 al 7.
    - A los números del 1 al 8, los relacionamos con los números del
      0 al 7.
    En el caso de que la coordenada ingresada sea una jugada en blanco, 
    la asociaremos con la coordenada (-1,-1).
    """
    
    if coordenada == '\n': return (-1,-1)

    columnas = ['A','B','C','D','E','F','G','H']

    columna = coordenada[0].upper()
    fila = int(coordenada[1])

    columnaEquivalente = columnas.index(columna)
    filaEquivalente = fila - 1

    return (columnaEquivalente,filaEquivalente)




def ocupada(tablero,coordenada):
    """
    verificacionOcupada :: list(list(str)) (int,int) -> bool

    Dado el tablero actual y una coordenada, nos indica si la casilla
    en donde se quiere realizar la jugada se encuentra ocupada o no.
    """
    
    columna,fila = coordenada

    return False if tablero[columna][fila] == "" else True




def posicionesPermitidas(turnoActual,fichasJugadas,tablero):
    """
    posicionesPermitidas :: str dict -> set((int,int))

    Dado el turno actual y las fichas que ya se colocaron en el tablero, 
    nos devuelve un conjunto de tuplas (que representan coordendas) de todas las
    casillas en las que se puede colocar una ficha. En caso de que no exista una 
    casilla permitida, el conjunto que se devuelve es vacío.
    """

    posicionesValidas = set()

    vecinasColorOpuesto = vecinasLibresFichasOpuestas(turnoActual,fichasJugadas,tablero)

    for coordenada in vecinasColorOpuesto:

        if fichasVolteadas(tablero, coordenada) != []:

            set.update([coordenada])

    return posicionesValidas



def vecinasLibresFichasOpuestas(turnoActual, fichasJugadas,tablero):
    """
    vecinasLibresFichaOpuesta :: str dict list(list(str)) -> set((int,int))

    Dado el turno actual, las fichas ya colocadas y el tablero, nos devuelve un conjunto
    con todas las casillas que son adyacentes a una ficha del color opuesto.
    """

    colorOpuesto = turnoOpuesto(turnoActual)

    vecinasFichasOpuestas = set()

    for coordenada in fichasJugadas[colorOpuesto]:

        set.update(vecinasLibres(coordenada,tablero))

    return vecinasFichasOpuestas

    



def vecinasLibres(coordenada,tablero):
    """
    vecinasLibres :: (int,int) -> set((int,int))

    Dada una coordenada y las fichas jugadas en el tablero, nos deveuelve
    un conjunto con todas las casillas adyacantes libres a dicha coordenada.
    """

    vecinas = set()

    columna,fila = coordenada

    for x in range(columna-1,columna+2):

        for y in range(fila-1,fila+2):

            if (0<= x <=7) and (0 <= y <= 7) and not ocupada(tablero,coordenada):

                vecinas.update([(x,y)])

    
    return vecinas


# COMPLETAR - FUNCION IMPORTANTE
def fichasVolteadas(tablero,coordenada):
    """
    fichasVolteadas :: list(list(str)) str -> list(tuple(int))

    Dado el tablero actual y una coordenada, nos devuelve una lista de
    tuplas, en donde cada una de las tuplas indica las coordenadas de
    las fichas que se dieron vuelta gracias a la colocación de la ficha
    pasada como argumento.
    Tenemos también 2 casos especiales:
    - Que la jugada no genéro cambios.
    - Que la jugada era un salteo de turno.
    En ambos casos la lista devuelta es vacía.
    """
    pass


def jugadaVerifica(jugadaActual,jugadasPosibles):
    """
    jugadaVerifica :: str set((int,int)) -> bool

    Dada la jugada actual leída del archivo de juego, y las posibles jugadas para
    realizar, nos determina si la jugada que se realizó es correcta o no.
    """
    
    
    if jugadaActual == '\n': # Salto de turno
        
        return True if jugadasPosibles == {} else False

    elif not verificacionRango or not verificacionFormato or ocupada: # No cumple con condiciones básicas

        return False

    
    coordenada = convertirCoordenadas(jugadaActual)

    return True if coordenada in jugadasPosibles else False
          


def darVueltaFichasTablero():
    """
    """
    pass


def actualizarFichasJugadas():
    """
    """
    pass





def volteadasHorizontalmente(tablero,coordenada,turnoActual):
    """
    volteadasHorizontalmente :: list(list(str)) (int,int) str -> list((int,int))

    Dado el tablero actual, la coordenada donde se coloca la ficha y el turno
    que estamos chequeando, nos devuelve una lista de todas las fichas que hizo que
    se den vuelta horizontalmente. En caso de que la lista sea vacía, no modificó 
    ninguna ficha.
    """
    
    columna,fila = coordenada

    colorOpuesto = turnoOpuesto(turnoActual)
    
    volteadasDerecha = []
    volteadasIzquierda = []
    
    # Recorremos hacia la derecha
    fichasOpuestas = []
    indice = columna + 1

    while indice <= 6 and tablero[indice][fila] == colorOpuesto:    
        
        fichasOpuestas += [(indice,fila)]

        if tablero[indice + 1][fila] == turnoActual:
            volteadasDerecha += fichasOpuestas
        
        indice += 1

    # Recorremos hacia la izquierda
    fichasOpuestas = []
    indice = columna - 1

    while indice >= 1 and tablero[indice][fila] == colorOpuesto:    

        fichasOpuestas += [(indice,fila)]

        if tablero[indice - 1][fila] == turnoActual:
            volteadasIzquierda = fichasOpuestas

        indice -= 1

    return volteadasDerecha + volteadasIzquierda




def volteadasVerticalmente(tablero,coordenada,turnoActual):
    """
    volteadasVerticalmente :: list(list(str)) (int,int) str -> list((int,int))

    Dado el tablero actual, la coordenada donde se coloca la ficha y el turno
    que estamos chequeando, nos devuelve una lista de todas las fichas que hizo que
    se den vuelta verticalmente. En caso de que la lista sea vacía, no modificó 
    ninguna ficha.
    """
    
    columna,fila = coordenada

    colorOpuesto = turnoOpuesto(turnoActual)
    
    volteadasArriba = []
    volteadasAbajo = []
    
    # Recorremos hacia arriba
    fichasOpuestas = []
    indice = fila + 1

    while indice <= 6 and tablero[columna][indice] == colorOpuesto:    
        
        fichasOpuestas += [(columna,indice)]

        if tablero[columna][indice + 1] == turnoActual:
            volteadasArriba += fichasOpuestas

        indice += 1

    # Recorremos hacia abajo
    fichasOpuestas = []
    indice = fila - 1

    while indice >= 1 and tablero[columna][indice] == colorOpuesto:    

        fichasOpuestas += [(columna,indice)]

        if tablero[columna][indice - 1] == turnoActual:
            volteadasAbajo = fichasOpuestas

        indice -= 1

    return volteadasArriba + volteadasAbajo





def volteadasDiagonalDescendiente(tablero,coordenada,turnoActual):
    """
    volteadasDiagonalDescendiente :: list(list(str)) (int,int) str -> list((int,int))

    Dado el tablero actual, la coordenada donde se coloca la ficha y el turno
    que estamos chequeando, nos devuelve una lista de todas las fichas que hizo que
    se den vuelta en la diagonal descendiente.
    En caso de que la lista sea vacía, no modificó ninguna ficha.
    """
    
    columna,fila = coordenada

    colorOpuesto = turnoOpuesto(turnoActual)
    
    volteadasMitad1 = []
    volteadasMitad2 = []
    
    # Recorremos hacia una mitad
    fichasOpuestas = []
    indiceX = columna + 1
    indiceY = fila + 1

    while indiceX <= 6 and indiceY <= 6  tablero[indiceX][indiceY] == colorOpuesto:    
        
        fichasOpuestas += [(indiceX,indiceY)]

        if tablero[indiceX + 1][indiceY + 1] == turnoActual:
            volteadasMitad1 += fichasOpuestas

        indiceX += 1
        indiceY += 1

    # Recorremos hacia la otra mitad
    fichasOpuestas = []
    indiceX = columna - 1
    indiceY = fila - 1

    while indiceX >= 1 and indiceY >= 1 tablero[indiceX][indiceY] == colorOpuesto:    

        fichasOpuestas += [(indiceX,indiceY)]

        if tablero[indiceX - 1][indiceY - 1] == turnoActual:
            volteadasMitad2 = fichasOpuestas

        indiceX -= 1
        indiceY -= 1

    return volteadasMitad1 + volteadasMitad2



def volteadasDiagonalAscendiente():
    """
    volteadasDiagonalAscendiente :: list(list(str)) (int,int) str -> list((int,int))

    Dado el tablero actual, la coordenada donde se coloca la ficha y el turno
    que estamos chequeando, nos devuelve una lista de todas las fichas que hizo que
    se den vuelta en la diagonal ascendiente.
    En caso de que la lista sea vacía, no modificó ninguna ficha.
    """
    
    columna,fila = coordenada

    colorOpuesto = turnoOpuesto(turnoActual)
    
    volteadasMitad1 = []
    volteadasMitad2 = []
    
    # Recorremos hacia una mitad
    fichasOpuestas = []
    indiceX = columna + 1
    indiceY = fila - 1

    while indiceX <= 6 and indiceY >= 1  tablero[indiceX][indiceY] == colorOpuesto:    
        
        fichasOpuestas += [(indiceX,indiceY)]

        if tablero[indiceX + 1][indiceY - 1] == turnoActual:
            volteadasMitad1 += fichasOpuestas

        indiceX += 1
        indiceY -= 1

    # Recorremos hacia la otra mitad
    fichasOpuestas = []
    indiceX = columna - 1
    indiceY = fila + 1

    while indiceX >= 1 and indiceY >= 1 tablero[indiceX][indiceY] == colorOpuesto:    

        fichasOpuestas += [(indiceX,indiceY)]

        if tablero[indiceX - 1][indiceY - 1] == turnoActual:
            volteadasMitad2 = fichasOpuestas
        
        indiceX -= 1
        indiceY += 1

    return volteadasMitad1 + volteadasMitad2



def turnoOpuesto(turnoActual):
    """
    turnoOpuesto :: str -> str

    Dado el turno actual del juego, nos devuelve el string correspondiente al turno
    del otro jugador.
    """

    return "B" if turnoActual == "N" else "N"

