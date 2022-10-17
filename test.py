#Test de todas las funciones

from tablero import inicializarTablero
from verificacion_fichas import *


# Tests de funciones de tablero

def test_inicializarTablero():

    assert inicializarTablero() == [["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","B","N","","",""],
                                    ["","","","N","B","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""]]




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
