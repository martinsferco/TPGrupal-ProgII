# Main.py - Agrupamos todas las funciones

from verificacion_archivo import *
from verificacion_jugadores import *

def main():
    
    archivo = ingresaArchivo()
    print(archivo)

    if not verificaDatos(archivo): # SI ALGUNO DE LOS DATOS PRELIMINARES ES INCORRECTO NO EJECUTA NADA.
        print('El archivo tiene fallos')
        return 
    
    print('El archivo es correcto.')

main()

#print(verificaDatos('juego3.txt'))