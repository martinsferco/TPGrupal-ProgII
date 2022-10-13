# func.py

"""
Variables utilizadas:

Ficha: Tuple
Tablero: List(Ficha)

Listado de funciones para hacer: 

. Inicializar tablero
. Determinar jugadores, que color le corresponde y quien inicia
. Escribir jugadas
    | Chequear que la ficha este dentro del tablero
    | Chequear que la ficha este en una posicion vacia
    | Chequear que la ficha este tangente a una ficha del otro color
    | Chequear que la ficha colocada encierre fichas del otro color
        || Horizontalmente
        || Verticalmente
        || Diagonalmente
    | Modificar el tablero, y repetir
. Mostrar el tablero
. Determinar el ganador (si es que lo hay)

P.D: Si un chequeo del paso escribir jugadas no se cumple, sale de la funcion,
especifica cual fue el error, muestra el tablero y termina.

"""