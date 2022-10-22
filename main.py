from archivos import *
from jugadores import *
from tablero import *
from fichas import *

def main():

    nombreArchivo = input("Introduzca el archivo de jugadas: ")

    while not ingresaArchivo(nombreArchivo): # Seguimos pidiendo el archivo si no se encuentra.
        nombreArchivo = input("Introduzca el archivo de jugadas: ")
    
    rutaArchivo = 'assets/' + nombreArchivo + '.txt'

    archivo = open(rutaArchivo, 'r') # Abre el archivo una vez encontrado

    if not verificaDatos(archivo): # Si alguno de los datos preliminares es incorrecto no ejecutamos nada.
        print('El archivo ingresado tiene fallos. No se podrá jugar la partida.')
        return 
    
    # Si llegó hasta acá, las condiciones preliminares son correctas.
    print('El archivo ingresado es correcto. La partida comenzará en unos instantes.') 

    archivo.seek(0) # Volvemos al comienzo del archivo.

    jugador1 = jugador(archivo.readline()) #fila 1 correspondiente al jugador 1
    jugador2 = jugador(archivo.readline()) #fila 2 correspondiente al jugador 2
    turnoInicial = normalizarLectura(archivo.readline())

    print('El jugador 1 es', jugador1[0], 'con el color', jugador1[1])
    print('El jugador 2 es', jugador2[0], 'con el color', jugador2[1])
    print('Inicia el color', turnoInicial)

    # A partir de ahora, ya tenemos las condiciones de inicio, los jugadores y el color que arranca.
    
    tam_tablero = 8

    fichasJugadas = inicializarFichasJugadas(tam_tablero)

    turnoActual = turnoInicial 

    jugadasPosibles = posicionesPermitidas(turnoActual,fichasJugadas,tam_tablero) # Vemos las posiciones válidas
    
    jugadaActual = normalizarLectura(archivo.readline()) # Leo la jugada en formato string
    
    while jugadaVerifica(jugadaActual,jugadasPosibles):
        
        jugadaActual = convertirCoordenadas(jugadaActual) 
        print(jugadaActual)
        fichasModificadas = fichasVolteadas(fichasJugadas,turnoActual,jugadaActual,tam_tablero)# Que fichas se dan vuelta
        
        fichasModificadas.update({jugadaActual}) # Agregamos la ficha actual para darla vuelta
        
        if len(fichasModificadas) != 1: # Vemos que la jugada actual no sea un salteo de turno
         
            fichasJugadas = actualizarFichasJugadas(fichasJugadas,fichasModificadas,turnoActual) # Modificamos fichas
        
    
        turnoActual = turnoOpuesto(turnoActual) # Cambiamos el turno

        jugadasPosibles = posicionesPermitidas(turnoActual,fichasJugadas,tam_tablero) # Vemos las nuevas posiciones válidas

        jugadaActual = normalizarLectura(archivo.readline()) # Leemos la nueva jugada
        
    archivo.close()    
    
    mostrarTablero(fichasJugadas,tam_tablero)




if __name__ == "__main__":
    main()


