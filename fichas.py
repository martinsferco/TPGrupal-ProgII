def verificacionFormato(coordenada):
    """
    verificacionFormato :: str -> bool

    La función toma un string leído del archivo de juego y 
    nos determina si tiene como primer valor un string y un número
    como segundo. También verifica que dicho string, tenga exactamente
    una longitud de dos.
    """
    
    if len(coordenada) != 2: # No verifica que tenga dos coordenadas 
        return False
    
    columna, fila = coordenada[0],coordenada[1]
        
    if not columna.isalpha(): # No verifica que la columna sea una letra
        return False

    if not fila.isdigit(): # No verifica que la fila sea un número
        return False

    return True



def verificacionRango(coordenada):
    """
    verificacionRango :: str -> bool

    Dado un string no vacío, nos determina si dicha coordenada
    se encuentra dentro de los límites del tablero.
    """
    
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
      del 0 al 7. - A los números del 1 al 8, los relacionamos con los números del 0 al 7.
    En el caso de que la coordenada ingresada sea una jugada en blanco, 
    la asociaremos con la coordenada (-1,-1).
    """
    
    if coordenada == '': return (-1,-1)

    columnas = ['A','B','C','D','E','F','G','H']

    columna = coordenada[0].upper()
    fila = int(coordenada[1])

    columnaEquivalente = columnas.index(columna)
    filaEquivalente = fila - 1

    return (columnaEquivalente,filaEquivalente)



def ocupada(fichasJugadas,coordenada):
    """
    verificacionOcupada :: dict(str:set((int,int))) (int,int) -> bool

    Dada las fichas jugadas y una coordenada, nos indica si la casilla
    en donde se quiere realizar la jugada se encuentra ocupada o no.
    """

    return (coordenada in fichasJugadas["B"]) or (coordenada in fichasJugadas["N"])



def posicionesPermitidas(turnoActual,fichasJugadas,tam_tablero):
    """
    posicionesPermitidas :: str dict(str:set((int,int))) int -> set((int,int))

    Dado el turno actual, las fichas que ya se colocaron en el tablero y su tamaño, 
    nos devuelve un conjunto de tuplas (que representan coordendas) de todas las
    casillas en las que se puede colocar una ficha. En caso de que no exista una 
    casilla permitida, el conjunto que se devuelve es vacío.
    """

    posicionesValidas = set()

    vecinasColorOpuesto = vecinasLibresFichasOpuestas(turnoActual,fichasJugadas,tam_tablero)
 
    for coordenada in vecinasColorOpuesto:

        if fichasVolteadas(fichasJugadas,turnoActual,coordenada,tam_tablero) != set():

            posicionesValidas.update([coordenada])

    return posicionesValidas



def vecinasLibresFichasOpuestas(turnoActual, fichasJugadas,tam_tablero):
    """
    vecinasLibresFichaOpuesta :: str dict(str:set((int,int))) int -> set((int,int))

    Dado el turno actual, las fichas ya colocadas y el tamaño del tablero, nos devuelve un conjunto
    con todas las casillas que son adyacentes a una ficha del color opuesto.
    """

    colorOpuesto = turnoOpuesto(turnoActual)

    vecinasFichasOpuestas = set()

    for coordenada in fichasJugadas[colorOpuesto]:

        vecinasFichasOpuestas.update(vecinasLibres(coordenada,fichasJugadas,tam_tablero))
        
    return vecinasFichasOpuestas

    

def vecinasLibres(coordenada,fichasJugadas,tam_tablero):
    """
    vecinasLibres :: (int,int) dict(str:set((int,int))) int-> set((int,int))

    Dada una coordenada de ficha, las fichas jugadas en el tablero y el tamaño del mismo,
    nos devuelve un conjunto con todas las casillas adyacantes libres a dicha ficha.
    """

    vecinas = set()

    columna,fila = coordenada

    for x in range(columna-1,columna+2):

        for y in range(fila-1,fila+2):

            if (0<= x <=(tam_tablero - 1)) and (0 <= y <=(tam_tablero - 1)) and not ocupada(fichasJugadas,(x,y)):

                vecinas.update([(x,y)])
 
    # Eliminamos la propia casilla
    vecinas.discard(coordenada)

    return vecinas



def fichasVolteadas(fichasJugadas,turnoActual,coordenada,tam_tablero):
    """
    fichasVolteadas : dict(str:set((int,int))) str (int,int) int -> set((int,int))

    Dadas las fichas jugadas, el turno actual, la coordenada que queremos chequear y
    el tamaño del tablero,nos devuelve un conjunto tuplas, en donde cada una de las
    tuplas indica las coordenadas de las fichas que se dieron vuelta gracias a la 
    colocación de la ficha pasada como argumento.

    Tenemos también 2 casos especiales:
    - Que la jugada no genéro cambios.
    - Que la jugada era un salteo de turno.
    En ambos casos el conjunto devuelto es vacío.
    """
    
    if coordenada == (-1,-1): # Salto de turno
        return set()
    
    # Vemos las volteadas en cada una de las direcciones
    horizontal = volteadasHorizontalmente(fichasJugadas,coordenada,turnoActual,tam_tablero)
    vertical = volteadasVerticalmente(fichasJugadas,coordenada,turnoActual,tam_tablero)
    diagonal1 = volteadasDiagonalDescendiente(fichasJugadas,coordenada,turnoActual,tam_tablero)
    diagonal2 = volteadasDiagonalAscendiente(fichasJugadas,coordenada,turnoActual,tam_tablero)
    
    return (horizontal | vertical | diagonal1 | diagonal2 )



def jugadaVerifica(jugadaActual,jugadasPosibles):
    """
    jugadaVerifica :: str set((int,int)) -> bool

    Dada la jugada actual leída del archivo de juego, y las posibles jugadas para
    realizar, nos determina si la jugada que se realizó es correcta o no.
    """
    
    if jugadaActual == '': # Cuando la jugada es un Salto de turno
        
        if jugadasPosibles != set():
            print ("Se salteó el turno cuando había jugadas posibles.")
            return False

        return True

    if not verificacionFormato(jugadaActual):
        print("La jugada no cumple con el formato estipulado.")
        return False

    if not verificacionRango(jugadaActual):
        print("La jugada se sale fuera del rango del tablero.")
        return False
   
    coordenada = convertirCoordenadas(jugadaActual)
    
    if coordenada not in jugadasPosibles:
        print("La jugada no se encuentra de las jugadas posibles.")
        return False

    return True
        


def actualizarFichasJugadas(fichasJugadas,fichasModificadas,turnoActual):
    """
    actualizarFichasJugadas :: dict(str:set((int,int))) list((int,int)) str -> dic(str:set((int,int)))

    Dada las fichas jugadas, las fichas que debemos modificar y el turno actual, 
    nos devuelve las nuevas posiciones de las fichas jugadas.
    """

    for ficha in fichasModificadas:

        fichasJugadas[turnoActual].update([ficha])
        fichasJugadas[turnoOpuesto(turnoActual)].discard(ficha)
   
    return fichasJugadas



def volteadasHorizontalmente(fichasJugadas,coordenada,turnoActual,tam_tablero):
    """
    volteadasHorizontalmente :: dict(str:set((int,int))) (int,int) str int -> set((int,int))

    Dadas las fichas jugadas, la coordenada donde se coloca la ficha, el turno
    que estamos chequeando y el tamaño del tablero, nos devuelve un conjunto de todas 
    las fichas que hizo que se den vuelta horizontalmente. En caso de que el conjunto
    sea vacío, no modificó ninguna ficha.
    """
    columna,fila = coordenada

    maximo = tam_tablero - 2

    colorOpuesto = turnoOpuesto(turnoActual)
    
    volteadasDerecha = set()
    volteadasIzquierda = set()
    
    # Recorremos hacia la derecha
    fichasOpuestas = []
    indice = columna + 1

    while indice <= maximo and (indice,fila) in fichasJugadas[colorOpuesto]:    
        
        fichasOpuestas += [(indice,fila)]

        if (indice + 1,fila) in fichasJugadas[turnoActual]:
            volteadasDerecha.update(fichasOpuestas)
        
        indice += 1

    # Recorremos hacia la izquierda
    fichasOpuestas = []
    indice = columna - 1

    while indice >= 1 and (indice,fila) in fichasJugadas[colorOpuesto]:    

        fichasOpuestas += [(indice,fila)]

        if (indice - 1,fila) in fichasJugadas[turnoActual]:
            volteadasIzquierda.update(fichasOpuestas)

        indice -= 1

    return (volteadasDerecha | volteadasIzquierda)



def volteadasVerticalmente(fichasJugadas,coordenada,turnoActual,tam_tablero):
    """
    volteadasVerticalmente :: dict(str:set((int,int))) (int,int) str int -> set((int,int))

    Dadas las fichas jugadas, la coordenada donde se coloca la ficha, el turno
    que estamos chequeando y el tamaño del tablero, nos devuelve un conjunto de todas
    las fichas que hizo que se den vuelta verticalmente. En caso de que el conjunto
    sea vacío, no modificó ninguna ficha.
    """
    
    columna,fila = coordenada

    maximo = tam_tablero - 2

    colorOpuesto = turnoOpuesto(turnoActual)
    
    volteadasArriba = set()
    volteadasAbajo = set()
    
    # Recorremos hacia arriba
    fichasOpuestas = []
    indice = fila + 1

    while indice <= maximo and (columna,indice) in fichasJugadas[colorOpuesto]:    
        
        fichasOpuestas += [(columna,indice)]

        if (columna,indice + 1) in fichasJugadas[turnoActual]:
            volteadasArriba.update(fichasOpuestas)

        indice += 1

    # Recorremos hacia abajo
    fichasOpuestas = []
    indice = fila - 1

    while indice >= 1 and (columna,indice) in fichasJugadas[colorOpuesto]:    

        fichasOpuestas += [(columna,indice)]

        if (columna,indice - 1) in fichasJugadas[turnoActual]:
            volteadasAbajo.update(fichasOpuestas)

        indice -= 1

    return volteadasArriba | volteadasAbajo



def volteadasDiagonalDescendiente(fichasJugadas,coordenada,turnoActual,tam_tablero):
    """
    volteadasDiagonalDescendiente :: dict(str:set((int,int))) (int,int) str int -> set((int,int))

    Dadas las fichas jugadas, la coordenada donde se coloca la ficha, el turno
    que estamos chequeando y el tamaño del tablero, nos devuelve un conjunto de 
    todas las fichas que hizo que se den vuelta en la diagonal descendiente.
    En caso de que el conjunto sea vacío, no modificó ninguna ficha.
    """
    
    columna,fila = coordenada

    maximo = tam_tablero - 2

    colorOpuesto = turnoOpuesto(turnoActual)
    
    volteadasMitad1 = set()
    volteadasMitad2 = set()
    
    # Recorremos hacia una mitad
    fichasOpuestas = []
    indiceX = columna + 1
    indiceY = fila + 1

    while indiceX <= maximo and indiceY <= maximo and (indiceX,indiceY) in fichasJugadas[colorOpuesto]:    
        
        fichasOpuestas += [(indiceX,indiceY)]

        if (indiceX + 1,indiceY + 1) in fichasJugadas[turnoActual]:
            volteadasMitad1.update(fichasOpuestas)

        indiceX += 1
        indiceY += 1

    # Recorremos hacia la otra mitad
    fichasOpuestas = []
    indiceX = columna - 1
    indiceY = fila - 1

    while indiceX >= 1 and indiceY >= 1 and (indiceX,indiceY) in fichasJugadas[colorOpuesto]:    

        fichasOpuestas += [(indiceX,indiceY)]

        if (indiceX - 1,indiceY - 1) in fichasJugadas[turnoActual]:
            volteadasMitad2.update(fichasOpuestas)

        indiceX -= 1
        indiceY -= 1

    return volteadasMitad1 | volteadasMitad2



def volteadasDiagonalAscendiente(fichasJugadas,coordenada,turnoActual,tam_tablero):
    """
    volteadasDiagonalAscendiente :: dict(str:set((int,int))) (int,int) str int -> set((int,int))

    Dadas las fichas jugadas, la coordenada donde se coloca la ficha, el turno que estamos
    que estamos chequeando y el tamaño del tablero, nos devuelve un conjunto de todas
    las fichas que hizo que se den vuelta en la diagonal ascendiente.
    En caso de que el conjunto sea sea vacío, no modificó ninguna ficha.
    """
    
    columna,fila = coordenada

    maximo = tam_tablero - 2

    colorOpuesto = turnoOpuesto(turnoActual)
    
    volteadasMitad1 = set()
    volteadasMitad2 = set()
    
    # Recorremos hacia una mitad
    fichasOpuestas = []
    indiceX = columna + 1
    indiceY = fila - 1

    while indiceX <= maximo and indiceY >= 1 and (indiceX,indiceY) in fichasJugadas[colorOpuesto]:    
        
        fichasOpuestas += [(indiceX,indiceY)]

        if (indiceX + 1,indiceY - 1) in fichasJugadas[turnoActual]:
            volteadasMitad1.update(fichasOpuestas)

        indiceX += 1
        indiceY -= 1

    # Recorremos hacia la otra mitad
    fichasOpuestas = []
    indiceX = columna - 1
    indiceY = fila + 1

    while indiceX >= 1 and indiceY <= maximo and (indiceX,indiceY) in fichasJugadas[colorOpuesto]:    

        fichasOpuestas += [(indiceX,indiceY)]

        if (indiceX - 1,indiceY + 1) in fichasJugadas[turnoActual]:
            volteadasMitad2.update(fichasOpuestas)
        
        indiceX -= 1
        indiceY += 1

    return volteadasMitad1 | volteadasMitad2



def turnoOpuesto(turnoActual):
    """
    turnoOpuesto :: str -> str

    Dado el turno actual del juego, nos devuelve el string correspondiente al turno
    del otro jugador.
    """

    return "B" if turnoActual == "N" else "N"



def normalizarLectura(jugada):
    """
    normalizarLectura :: str -> str
       
    Dado un string de un renglón del archivo de juego, nos devuelve el mismo
    string pero quitándole la terminación del salto de línea '\n' y haciendo
    que todas las letras sean mayúsculas.
    """
    
    return jugada[:-1].upper()
