from tablero import inicializarTablero
from fichas import *
from jugadores import *



# Tests de funciones de tablero

def test_inicializarTablero():

    assert inicializarTablero() == [["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","B","N","","",""],
                                    ["","","","N","B","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""]]



# Test de funciones de verificación de archivos

def test_verificaDatos():
    # Ver como se podría testear

    pass









# Tests de funciones de verificación de información de jugadores

def test_jugador():

    assert jugador('Martin, N\n') == ('Martin', 'N')
    assert jugador('Raul, B\n') == ('Raul', 'B')


def test_coloresCorrectos():

    assert coloresCorrectos(('Martin', 'N'), ('Raul', 'B')) == True
    assert coloresCorrectos(('Martin', 'R'), ('Raul', 'V')) == False



















# Tests de funciones de verificación de fichas

def test_verificacionFormato():
    
    assert not verificacionFormato("B23")
    assert not verificacionFormato("AA2")
    assert not verificacionFormato("22")
    assert not verificacionFormato("AA")
    assert verificacionFormato("A1")


def test_verfificacionRango():

    assert not verificacionRango("B23") 
    assert not verificacionRango("A9")
    assert not verificacionRango("Z2")
    assert verificacionRango("A1")
    

def test_convertirCoordenadas():
    
    assert convertirCoordenadas("A1") == (0,0)
    assert convertirCoordenadas("H8") == (7,7)
    assert convertirCoordenadas("C4") == (2,3)
    assert convertirCoordenadas("E5") == (4,4)


def test_ocupada():
    fichasJugadas = {"B":{(4,4),(3,3)},"N":{(3,4),(4,3)}}

    assert ocupada(fichasJugadas,(4,4))
    assert ocupada(fichasJugadas,(4,3))
    assert not ocupada(fichasJugadas,(0,0))


def test_posicionesPermitidas():
    fichasJugadas = {"B":{(4,4),(3,3)},"N":{(3,4),(4,3)}}

    assert posicionesPermitidas("B",fichasJugadas) == {(4,2),(2,4),(3,5),(5,3)}
    assert posicionesPermitidas("N",fichasJugadas) == {(3,2),(2,3),(4,5),(5,4)}

def test_vecinasLibresFichasOpuestas():
    fichasJugadas = {"B":{(4,4),(3,3)},"N":{(3,4),(4,3)}}
    
    assert vecinasLibresFichasOpuestas("B",fichasJugadas) == {(2,3),(2,4),(2,5),(3,5),(4,5),(5,2),(5,3),(5,4),(4,2),(3,2)}
    assert vecinasLibresFichasOpuestas("N",fichasJugadas) == {(2,2),(2,3),(2,4),(3,5),(4,5),(5,5),(5,3),(5,4),(4,2),(3,2)} 

def test_vecinasLibres():
    fichasJugadas = {"B":{(4,4),(3,3)},"N":{(3,4),(4,3)}}

    assert vecinasLibres((4,4),fichasJugadas) == {(5,3),(5,4),(5,5),(3,5),(4,5)}
    assert vecinasLibres((3,4),fichasJugadas) == {(2,3),(2,4),(2,5),(3,5),(4,5)}
    assert vecinasLibres((0,0),fichasJugadas) == {(1,0),(1,1),(0,1)}
    assert vecinasLibres((4,0),fichasJugadas) == {(3,0),(3,1),(4,1),(5,0),(5,1)}

def test_fichasVolteadas():
    pass


def test_jugadaVerifica():
    pass


def test_darVueltaFichasTablero():
    pass


def test_actualizarFichasJugadas():
    pass


def test_volteadasHorizontalmente():
    pass


def test_volteadasVerticalmente():
    pass


def test_volteadasDiagonalDescendiente():
    pass


def test_volteadasDiagonalAscendiente():
    pass


def test_turnoOpuesto():

    assert turnoOpuesto("B") == "N"
    assert turnoOpuesto("N") == "B"
