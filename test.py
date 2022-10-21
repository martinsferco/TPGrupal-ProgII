from tablero import inicializarTablero
from fichas import *
from jugadores import *
from archivos import ingresaArchivo


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

# Test de funciones de ingreso de archivo

def test_ingresaArchivo():

    assert ingresaArchivo('juego1') == True
    assert ingresaArchivo('hola') == False
    assert ingresaArchivo('lcc') == False
    assert ingresaArchivo('juego2') == True


















# Tests de funciones de verificación de fichas

def test_verificacionFormato():
    
    assert not verificacionFormato("B23")
    assert not verificacionFormato("AA2")
    assert not verificacionFormato("22")
    assert not verificacionFormato("AA")
    assert verificacionFormato("A1")


def test_verfificacionRango():

    assert not verificacionRango("A9")
    assert not verificacionRango("Z2")
    assert verificacionRango("B3") 
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



def test_jugadaVerifica():
    posicionesPermitidas1 = {(4,2),(2,4),(3,5),(5,3)}
    posicionesPermitidas2 = set()

    assert not jugadaVerifica("55",posicionesPermitidas1) 
    assert not jugadaVerifica("BB",posicionesPermitidas1)
    assert not jugadaVerifica("ZZ1",posicionesPermitidas1)
    assert not jugadaVerifica("A9",posicionesPermitidas1)
    assert not jugadaVerifica("Z2",posicionesPermitidas1)
    assert not jugadaVerifica("",posicionesPermitidas1)
    assert jugadaVerifica("",posicionesPermitidas2)
    assert jugadaVerifica("E3",posicionesPermitidas1)
    assert not jugadaVerifica("A1",posicionesPermitidas1)


def test_darVueltaFichasTablero():
    tablero = inicializarTablero()
    
    tableroModificado1 = tablero
    tableroModificado1[3][3],tableroModificado1[2][3] = "N","N"

    tableroModificado2 = tablero
    tableroModificado2[4][2],tableroModificado2[4][3] = "B","B"

    assert darVueltaFichasTablero(tablero,"N",[(3,3),(2,3)]) == tableroModificado1
    assert darVueltaFichasTablero(tablero,"B",[(4,2),(4,3)]) == tableroModificado2

def test_actualizarFichasJugadas():
    
    fichasModificadas = {(4,2),(4,3),(2,4),(3,4),(2,6),(3,5)}

    fichasJugadas1 = {"B":{(4,1),(1,4),(1,7)},"N":{(4,2),(4,3),(2,4),(3,4),(2,6),(3,5),(5,4),(5,5)}}
    
    resultado1 = {"B":{(4,1),(1,4),(1,7),(4,2),(4,3),(2,4),(3,4),(2,6),(3,5)},"N":{(5,4),(5,5)}}

    assert actualizarFichasJugadas(fichasJugadas1,fichasModificadas,"B") == resultado1
    



def test_fichasVolteadas():
    
    fichas = {(2,2),(3,3),(5,5),(6,6),(2,6),(3,5),(5,3),(6,2),(2,4),(3,4),(5,4),(6,4),(4,2),(4,3),(4,5),(4,6)}

    fichasJugadas1 = {"B":{(1,1),(4,1),(7,1),(1,4),(1,7),(4,7),(7,4),(7,7)},"N":fichas}
    fichasJugadas2 = {"N":{(1,1),(4,1),(7,1),(1,4),(1,7),(4,7),(7,4),(7,7)},"B":fichas}

    assert fichasVolteadas(fichasJugadas1,"B",(4,4)) == fichas
    assert fichasVolteadas(fichasJugadas2,"N",(4,4)) == fichas



def test_volteadasHorizontalmente():

    fichasJugadas1 = {"B":{(1,4),(7,4)},"N":{(2,4),(3,4),(5,4),(6,4)}}
    fichasJugadas2 = {"B":{(0,4)},"N":{(2,4),(3,4),(5,4),(6,4)}}
    
    fichasJugadas3 = {"N":{(1,4),(7,4)},"B":{(2,4),(3,4),(5,4),(6,4)}}
    fichasJugadas4 = {"N":{(0,4)},"B":{(2,4),(3,4),(5,4),(6,4)}}

    assert volteadasHorizontalmente(fichasJugadas1,(4,4),"B") == {(2,4),(3,4),(5,4),(6,4)}
    assert volteadasHorizontalmente(fichasJugadas2,(4,4),"B") == set()
    
    assert volteadasHorizontalmente(fichasJugadas3,(4,4),"N") == {(2,4),(3,4),(5,4),(6,4)}
    assert volteadasHorizontalmente(fichasJugadas4,(4,4),"N") == set()



def test_volteadasVerticalmente():

    fichasJugadas1 = {"B":{(4,1),(4,7)},"N":{(4,2),(4,3),(4,5),(4,6)}}
    fichasJugadas2 = {"B":{(4,0)},"N":{(2,4),(3,4),(5,4),(6,4)}}
    
    fichasJugadas3 = {"N":{(4,1),(4,7)},"B":{(4,2),(4,3),(4,5),(4,6)}}
    fichasJugadas4 = {"N":{(4,0)},"B":{(2,4),(3,4),(5,4),(6,4)}}
    
    assert volteadasVerticalmente(fichasJugadas1,(4,4),"B") == {(4,2),(4,3),(4,5),(4,6)}
    assert volteadasVerticalmente(fichasJugadas2,(4,4),"B") == set()
    
    assert volteadasVerticalmente(fichasJugadas3,(4,4),"N") == {(4,2),(4,3),(4,5),(4,6)}
    assert volteadasVerticalmente(fichasJugadas4,(4,4),"N") == set()



def test_volteadasDiagonalDescendiente():

    fichasJugadas1 = {"B":{(1,1),(7,7)},"N":{(2,2),(3,3),(5,5),(6,6)}}
    fichasJugadas2 = {"B":{(0,0)},"N":{(2,2),(3,3),(5,5),(6,6)}}
    
    fichasJugadas3 = {"N":{(1,1),(7,7)},"B":{(2,2),(3,3),(5,5),(6,6)}}
    fichasJugadas4 = {"N":{(0,0)},"B":{(2,2),(3,3),(5,5),(6,6)}}
    

    assert volteadasDiagonalDescendiente(fichasJugadas1,(4,4),"B") == {(2,2),(3,3),(5,5),(6,6)}
    assert volteadasDiagonalDescendiente(fichasJugadas2,(4,4),"B") == set()
    
    assert volteadasDiagonalDescendiente(fichasJugadas3,(4,4),"N") == {(2,2),(3,3),(5,5),(6,6)}
    assert volteadasDiagonalDescendiente(fichasJugadas4,(4,4),"N") == set()



def test_volteadasDiagonalAscendiente():

    fichasJugadas1 = {"B":{(7,1),(1,7)},"N":{(6,2),(5,3),(3,5),(2,6)}}
    fichasJugadas2 = {"B":{(1,7)},"N":{(7,1),(6,2),(5,3),(3,5)}}
    
    fichasJugadas3 = {"N":{(7,1),(1,7)},"B":{(6,2),(5,3),(3,5),(2,6)}}
    fichasJugadas4 = {"N":{(1,7)},"B":{(7,1),(6,2),(5,3),(3,5)}}

    assert volteadasDiagonalAscendiente(fichasJugadas1,(4,4),"B") == {(6,2),(5,3),(3,5),(2,6)}
    assert volteadasDiagonalAscendiente(fichasJugadas2,(4,4),"B") == set()
    
    assert volteadasDiagonalAscendiente(fichasJugadas3,(4,4),"N") == {(6,2),(5,3),(3,5),(2,6)}
    assert volteadasDiagonalAscendiente(fichasJugadas4,(4,4),"N") == set()



def test_turnoOpuesto():

    assert turnoOpuesto("B") == "N"
    assert turnoOpuesto("N") == "B"


def test_normalizarLectura():

    assert normalizarLectura("B5\n") == "B5"
    assert normalizarLectura("N\n") == "N"
