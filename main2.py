
fichasNegras = {(4,4),(4,3)} # Tiene las dos fichas centrales negras.
fichasBlancas = {(3,3),(4,4)} # Tiene las dos fichas centrales blancas.

fichasJugadas = {"B":fichasBlancas,"N":fichasNegras}

cantidadFichasNegras = len(fichasNegras)
cantidadFichasBlancas = len(fichasBlancas)

turnoActual = archivo.readline()

posiblesJugadas = actualesPosiblesJugadas(tablero,turnoActual,fichasJugadas) # Vemos que jugadas se pueden realizar

jugadaActual = archivo.readline() # Vemos la jugada actual

while jugadaVerifica(jugadaActual,posiblesJugadas): # Verificamos que sea una jugada valida
    
    jugadaActual = convertirCoordenadas()

    fichasVolteadas = fichasVolteadas(jugadaActual, tablero) # Vemos que fichas se dan vuelta con dicha jugada

    tablero = darVueltaFichasTablero() # Modificamos el tablero

    # Modificamos las fichas de cada color
    fichasJugadas[turnoActual],fichasJugadas[turnoOpuesto(turnoActual)] = cambiarCantidadFichas(fichasJugadas,fichasVolteadas)

    # Modificamos las cantidades de fichas de cada color (se puede mejorar y no usar len())
    cantidadFichasNegras, cantidadFichasBlancas = len(fichasJugadas["N"]),len(fichasJugadas["B"])

    turnoActual = turnoOpuesto(turnoActual) # Cambiamos el turno
 
    posiblesJugadas = actualesPosiblesJugadas(tablero,turnoActual,fichasJugadas[turnoOpuesto(turnoActual)]) # Vemos que jugadas se realizan con el nuevo tablero

    jugadaActual = archivo.readline() # Vemos la nueva jugada

    # Y repetimos nuevamente el ciclo
    
# Finalmente mostramos el tablero
mostrarTablero(tablero)




