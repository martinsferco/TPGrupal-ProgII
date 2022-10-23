def inicializarFichasJugadas(tam_tablero):
    """ 
    inicializarFichasJugadas:: int -> dict(str:set((int,int)))

    La función nos devuelve un diccionario de las fichas negras y blancas jugadas,
    colocadas inicialmente.
    Cada una de las claves de color está relacionada con un conjunto de tuplas, que
    representan las coordenadas de donde se encuentras las fichas del respectivo
    color.
    """
            
    fichaBlanca = "B"
    fichaNegra = "N"
        
    fichasJugadas = {fichaBlanca:set(),fichaNegra:set()}

    # Generamos los 2 valores de coordenadas de fichas centrales
    coordenada1 = tam_tablero // 2
    coordenada2 = (tam_tablero // 2) - 1
    
    # Agregamos las coordenadas de las 4 fichas centrales
    fichasJugadas[fichaBlanca].update([(coordenada1,coordenada1),(coordenada2,coordenada2)])
    fichasJugadas[fichaNegra].update([(coordenada1,coordenada2),(coordenada2,coordenada1)])

    return fichasJugadas



def mostrarTablero(fichasJugadas,tam_tablero):
    """
    mostrarTablero :: dict(str:set((int,int))) int -> None

    Dadas las fichas jugadas de cada color y el tamaño del tablero,
    la función imprime en pantalla una representación del mismo.
    """
    
    fichaBlanca = "B "
    fichaNegra = "N "

    #Imprimimos el tablero

    for fila in range(tam_tablero):
        
        print("\n-------------------------")

        for columna in range(tam_tablero):

            if (columna,fila) in fichasJugadas["B"]:
                print(f'|{fichaBlanca}',end = "")

            elif (columna,fila) in fichasJugadas["N"]:
                print(f'|{fichaNegra}',end = "")
             
            else:
                print('|  ',end = "")

        print('|',end = "")

    print("\n-------------------------")




