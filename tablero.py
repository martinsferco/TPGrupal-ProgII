#Inicialización tablero y mostrar tablero

def inicializarTablero():
    """ 
    inicializarTablero:: None -> list(List(str))

    La función nos devuelve un tablero de partida vacío, excepto
    por las 4 fichas centrales.
    """
            
    fichaBlanca = "B"
    fichaNegra = "N"


    #Inicializamos tablero vacío
    tablero = [ ["" for fila in range(8)] for columna in range(8)]
    
    #Seteamos las fichas centrales
    tablero[3][3] = fichaBlanca
    tablero[4][4] = fichaBlanca
    tablero[3][4] = fichaNegra
    tablero[4][3] = fichaNegra

    return tablero


def mostrarTablero(tablero):
    """
    mostrarTablero :: list(list(str)) -> None

    Dado un tablero, la función imprime en pantalla una representación
    del mismo.
    """
    
    fichaBlanca = "⚪"
    fichaNegra = "⚫"

    #Imprimimos el tablero

    for fila in range(8):
        
        print("\n-------------------------")

        for columna in tablero:

            if columna[fila] == "":
                print('|  ',end = "")

            if columna[fila] == "B":
                print(f'|{fichaBlanca}',end = "")

            if columna[fila] == "N":
                print(f'|{fichaNegra}',end = "")
        
        print('|',end = "")

    print("\n-------------------------")




