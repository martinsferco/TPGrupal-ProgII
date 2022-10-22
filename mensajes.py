from time import sleep

def mensajeProcesamientoArchivo(nombreArchivo):
    """
    mensajeProcesamientoArchivo :: str -> None

    Nos muestra un mensaje indicando que se está procesando el archivo.
    """

    print(f'\nEl archivo {nombreArchivo}.txt se está procesando ...')
    sleep(1)



def errorJugada(jugada):
    """
    errorJugada :: str -> None

    Nos indica que en la jugada se produjo un error
    """
