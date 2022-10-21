from archivos import *
from jugadores import *
from tablero import *
from fichas import *

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
    turnoInicial = archivo.readline()[:-1] # Eliminamos el '\n'

    print('El jugador 1 es', jugador1[0], 'con el color', jugador1[1])
    print('El jugador 2 es', jugador2[0], 'con el color', jugador2[1])
    print('Inicia el color', turnoInicial)

    # A partir de ahora, ya tenemos las condiciones de inicio, los jugadores y el color que arranca.
    





    # Ver si le pasamos el tamaño
    tablero = inicializarTablero()
    
    fichasJugadas = {"B":{(3,3),(4,4)},"N":{(3,4),(4,3)}}

    turnoActual = turnoInicial 

    jugadasPosibles = posicionesPermitidas(turnoActual,fichasJugadas) # Vemos las posiciones válidas
    
    jugadaActual = archivo.readline() # Leo la jugada en formato string
    
    while jugadaVerifica(jugadaActual,jugadasPosibles):

        jugadaActual = convertirCoordenadas(jugadaActual) 

        fichasModificadas = fichasVolteadas(fichasJugadas,turnoActual,jugadaActual) + [jugadaActual] # Que fichas se dan vuelta

        if len(fichasModificadas) != 1: # Vemos que la jugada actual no sea un salteo de turno
         
            tablero = darVueltaFichasTablero(tablero,turnoActual,fichasModificadas) # Modificamos nuestro tablero
    
            fichasJugadas = actualizarFichasJugadas(fichasJugadas,fichasModificadas,turnoActual) # Modificamos fichas
        
        mostrarTablero(tablero)

        turnoActual = turnoOpuesto(turnoActual) # Cambiamos el turno

        jugadasPosibles = posicionesPermitidas(turnoActual,fichasJugadas) # Vemos las posiciones válidas

        jugadaActual = archivo.readline() # Leemos la nueva jugada
        
    archivo.close()
    
    print("Cantidad fichas: ",len(fichasJugadas["B"])+len(fichasJugadas["N"]))
    mostrarTablero(tablero)




if __name__ == "__main__":
    main()


#print(verificaDatos('juego3.txt'))
