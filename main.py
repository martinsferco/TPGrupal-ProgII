# Main.py - Agrupamos todas las funciones

from archivos import *
from jugadores import *
from tablero import *


def main():
    
    archivo = ingresaArchivo()
    print(archivo)

    if not verificaDatos(archivo): # SI ALGUNO DE LOS DATOS PRELIMINARES ES INCORRECTO NO EJECUTA NADA.
        print('El archivo tiene fallos')
        return 
    
    print('El archivo es correcto.') # SI LLEGO HASTA ACA, LAS CONDICIONES PRELIMINARES SE CUMPLEN.

    archivo.seek(0) # VUELVE AL COMIENZO DEL ARCHIVO. ANTERIORMENTE ESTABA EN LA FILA 3

    jugador1 = jugador(archivo.readline())
    jugador2 = jugador(archivo.readline())

    print('El jugador 1 es', jugador1[0], 'con el color', jugador1[1])
    print('El jugador 2 es', jugador2[0], 'con el color', jugador2[1])
    print('Inicia el color', archivo.readline())

    # == A PARTIR DE ACA, YA TENEMOS LAS CONDICIONES DE INICIO, LOS JUGADORES Y EL COLOR QUE INICIA. LISTO PARA INICIAR == 

    # Nota: en la asignacion de jugador1 y 2, poniendo archivo.readline() ya hace que avance una linea, no hace falta una variable
    # especifica 
    


    


if __name__ == "__main__":
    main()

#print(verificaDatos('juego3.txt'))
