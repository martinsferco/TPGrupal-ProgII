from archivos import *
from jugadores import *
from tablero import *
from os import system

def main():

    
    archivo = ingresaArchivo()
    print(archivo)

    # Si alguno de los datos preliminares es incorrecto no ejecutamos nada.
    if not verificaDatos(archivo):
        print('El archivo ingresado tiene fallos. No se podrá jugar la partida.')
        return 
    
    # Si llegó hasta acá, las condiciones preliminares son correctas.
    print('El archivo ingresado es correcto. La partida comenzará en unos instantes.') 

    archivo.seek(0) # Volvemos al comienzo del archivo.

    jugador1 = jugador(archivo.readline())
    jugador2 = jugador(archivo.readline())

    print('El jugador 1 es', jugador1[0], 'con el color', jugador1[1])
    print('El jugador 2 es', jugador2[0], 'con el color', jugador2[1])
    print('Inicia el color', archivo.readline())

    # A partir de ahora, ya tenemos las condiciones de inicio, los jugadores y el color que arranca.
    





    # Ver si le pasamos el tamaño
    tablero = inicializarTablero()
    
    fichasJugadas = {"B":{(3,3),(4,4)},"N":{(3,4),(4,3)}}
a
    turnoActual = archivo.readline() # Lo leo en formato string

    jugadasPosibles = posicionesPermitidas(turnoActual,fichasJugadas)

    jugadaActual = arhivo.readline() # Leo la jugada en formato string

    while jugadaVerifica(jugadaActual,jugadasPosibles):

        jugadaActual = convertirCoordenadas()

        fichasModificadas = fichasVolteadas(jugadaActual,tablero)

        tablero = darVueltaFichasTablero(tablero,jugadaActual,fichasModificadas)
    
        fichasJugadas[turnoActual],fichasJugadas[turnoOpuesto(turnoActual)] = actualizarFichasJugadas(fichasJugadas,fichasVolteadas)

        turnoActual = turnoOpuesto(turnoActual)

        # Repetimos todo lo anterior


    mostrarTablero(tablero)




if __name__ == "__main__":
    main()

#print(verificaDatos('juego3.txt'))
