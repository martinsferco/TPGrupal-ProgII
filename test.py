from tablero import inicializarTablero
from verificacion_fichas import *
from verificacion_jugadores import *



# Tests de funciones de tablero

def test_inicializarTablero():

    assert inicializarTablero() == [["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","B","N","","",""],
                                    ["","","","N","B","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""]]



# Test de funciones de verificación de archivos

def test_verificaDatos():

    assert verificaDatos('juego3.txt') ==  True



# Tests de funciones de verificación de información de jugadores

def test_jugador():

    assert jugador('Martin,N') == ('Martin', 'N')
    assert jugador('Raul,B') == ('Raul', 'B')


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
    

def test_verificacionOcupada():
    pass


def test_convertirCoordenada():
    
    assert convertirCoordenada("A1") == (0,0)
    assert convertirCoordenada("H8") == (7,7)
    assert convertirCoordenada("C4") == (2,3)
    assert convertirCoordenada("E5") == (4,4)


def test_fichasVolteadas():
    pass

