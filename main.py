from archivos import *
from jugadores import *
from tablero import *
from fichas import *
from mensajes import *

def main():

    nombreArchivo = input("\nIntroduzca el archivo de jugadas (sin extensión .txt): ")

    while not ingresaArchivo(nombreArchivo): # Seguimos pidiendo el archivo si no se encuentra.
        nombreArchivo = input("\nIntroduzca nuevamente el archivo de jugadas: ")
    
    rutaArchivo = 'assets/' + nombreArchivo + '.txt'

    archivo = open(rutaArchivo, 'r') # Abre el archivo una vez encontrado
    
    mensajeProcesamientoArchivo(nombreArchivo)

    if not verificaDatos(archivo): # Si alguno de los datos preliminares es incorrecto no ejecutamos nada.
        print('El archivo ingresado tiene fallos. No se podrá jugar la partida.')
        return 
    
    # Si llegó hasta acá, las condiciones preliminares son correctas.
    print('El archivo ingresado es correcto. A continuación presentamos a los jugadores:') 

    archivo.seek(0) # Volvemos al comienzo del archivo.

    jugador1 = jugador(archivo.readline()) #fila 1 correspondiente al jugador 1
    jugador2 = jugador(archivo.readline()) #fila 2 correspondiente al jugador 2
    turnoInicial = normalizarLectura(archivo.readline())

    informacionJugadores(jugador1,jugador2,turnoInicial)

    tam_tablero = 8

    fichasJugadas = inicializarFichasJugadas(tam_tablero)
    
    numeroFichasColocadas = 4

    turnoActual = turnoInicial 

    jugadasPosibles = posicionesPermitidas(turnoActual,fichasJugadas,tam_tablero) # Vemos las posiciones válidas
    
    jugadaActual = (archivo.readline()).upper() # Leemos la primer jugada

 
    while jugadaActual != "" and numeroFichasColocadas < 64 and jugadaVerifica(jugadaActual,jugadasPosibles,fichasJugadas):
    
        jugadaActual = convertirCoordenadas(jugadaActual) 
        
        fichasModificadas = fichasVolteadas(fichasJugadas,turnoActual,jugadaActual,tam_tablero)# Que fichas se dan vuelta
        
        fichasModificadas.update({jugadaActual}) # Agregamos la ficha actual para darla vuelta
        
        if len(fichasModificadas) != 1: # Vemos que la jugada actual no sea un salteo de turno
         
            fichasJugadas = actualizarFichasJugadas(fichasJugadas,fichasModificadas,turnoActual) # Modificamos fichas
            
            numeroFichasColocadas += 1

        turnoActual = turnoOpuesto(turnoActual) # Cambiamos el turno

        jugadasPosibles = posicionesPermitidas(turnoActual,fichasJugadas,tam_tablero) # Vemos las nuevas posiciones válidas

        jugadaActual = archivo.readline().upper() # Leemos la nueva jugada
        
    
    archivo.close()    
    
    mensajeFinalJuego(jugadaActual,fichasJugadas,turnoActual)    

    mostrarTablero(fichasJugadas,tam_tablero)




if __name__ == "__main__":
    main()


