from tablero import inicializarFichasJugadas
from fichas import *
from jugadores import *
from archivos import ingresaArchivo


# Tests de funciones de tablero

def test_inicializarFichasJugadas():

    assert inicializarFichasJugadas(8) == {"B":{(4,4),(3,3)},"N":{(3,4),(4,3)}}



# Tests de funciones de verificación de archivos

def test_verificaDatos():
    pass



def test_ingresaArchivo():

    assert ingresaArchivo('juego1')
    assert ingresaArchivo('juego2')
    assert not ingresaArchivo('hola')
    assert not ingresaArchivo('lcc')



# Tests de funciones de verificación de información de jugadores

def test_jugador():

    assert jugador('Martin,N') == ('Martin', 'N')
    assert jugador('Raul,B') == ('Raul', 'B')



def test_coloresCorrectos():

    assert coloresCorrectos(('Martin', 'N'), ('Raul', 'B')) 
    assert coloresCorrectos(('Martin', 'B'), ('Raul', 'N')) 
    assert not coloresCorrectos(('Martin', 'R'), ('Raul', 'V'))
    assert not coloresCorrectos(('Martin','B'),('Raul','B')) 



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

    assert posicionesPermitidas("B",fichasJugadas,8) == {(4,2),(2,4),(3,5),(5,3)}
    assert posicionesPermitidas("N",fichasJugadas,8) == {(3,2),(2,3),(4,5),(5,4)}



def test_vecinasLibresFichasOpuestas():
    fichasJugadas = {"B":{(4,4),(3,3)},"N":{(3,4),(4,3)}}
    
    assert vecinasLibresFichasOpuestas("B",fichasJugadas,8) == {(2,3),(2,4),(2,5),(3,5),(4,5),(5,2),(5,3),(5,4),(4,2),(3,2)}
    assert vecinasLibresFichasOpuestas("N",fichasJugadas,8) == {(2,2),(2,3),(2,4),(3,5),(4,5),(5,5),(5,3),(5,4),(4,2),(3,2)} 



def test_vecinasLibres():
    fichasJugadas = {"B":{(4,4),(3,3)},"N":{(3,4),(4,3)}}

    assert vecinasLibres((4,4),fichasJugadas,8) == {(5,3),(5,4),(5,5),(3,5),(4,5)}
    assert vecinasLibres((3,4),fichasJugadas,8) == {(2,3),(2,4),(2,5),(3,5),(4,5)}
    assert vecinasLibres((0,0),fichasJugadas,8) == {(1,0),(1,1),(0,1)}
    assert vecinasLibres((4,0),fichasJugadas,8) == {(3,0),(3,1),(4,1),(5,0),(5,1)}



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



def test_actualizarFichasJugadas():
    
    fichasModificadas = {(4,2),(4,3),(2,4),(3,4),(2,6),(3,5)}

    fichasJugadas1 = {"B":{(4,1),(1,4),(1,7)},"N":{(4,2),(4,3),(2,4),(3,4),(2,6),(3,5),(5,4),(5,5)}}
    resultado1 = {"B":{(4,1),(1,4),(1,7),(4,2),(4,3),(2,4),(3,4),(2,6),(3,5)},"N":{(5,4),(5,5)}}

    fichasJugadas2 = {"N":{(4,1),(1,4),(1,7)},"B":{(4,2),(4,3),(2,4),(3,4),(2,6),(3,5),(5,4),(5,5)}}
    resultado2 = {"N":{(4,1),(1,4),(1,7),(4,2),(4,3),(2,4),(3,4),(2,6),(3,5)},"B":{(5,4),(5,5)}}
    
    assert actualizarFichasJugadas(fichasJugadas1,fichasModificadas,"B") == resultado1
    assert actualizarFichasJugadas(fichasJugadas2,fichasModificadas,"N") == resultado2
        


def test_fichasVolteadas():
    
    fichas = {(2,2),(3,3),(5,5),(6,6),(2,6),(3,5),(5,3),(6,2),(2,4),(3,4),(5,4),(6,4),(4,2),(4,3),(4,5),(4,6)}

    fichasJugadas1 = {"B":{(1,1),(4,1),(7,1),(1,4),(1,7),(4,7),(7,4),(7,7)},"N":fichas}
    fichasJugadas2 = {"N":{(1,1),(4,1),(7,1),(1,4),(1,7),(4,7),(7,4),(7,7)},"B":fichas}

    assert fichasVolteadas(fichasJugadas1,"B",(4,4),8) == fichas
    assert fichasVolteadas(fichasJugadas2,"N",(4,4),8) == fichas



def test_volteadasHorizontalmente():

    fichasJugadas1 = {"B":{(1,4),(7,4)},"N":{(2,4),(3,4),(5,4),(6,4)}}
    fichasJugadas2 = {"B":{(0,4)},"N":{(2,4),(3,4),(5,4),(6,4)}}
    
    fichasJugadas3 = {"N":{(1,4),(7,4)},"B":{(2,4),(3,4),(5,4),(6,4)}}
    fichasJugadas4 = {"N":{(0,4)},"B":{(2,4),(3,4),(5,4),(6,4)}}

    assert volteadasHorizontalmente(fichasJugadas1,(4,4),"B",8) == {(2,4),(3,4),(5,4),(6,4)}
    assert volteadasHorizontalmente(fichasJugadas2,(4,4),"B",8) == set()
    
    assert volteadasHorizontalmente(fichasJugadas3,(4,4),"N",8) == {(2,4),(3,4),(5,4),(6,4)}
    assert volteadasHorizontalmente(fichasJugadas4,(4,4),"N",8) == set()



def test_volteadasVerticalmente():

    fichasJugadas1 = {"B":{(4,1),(4,7)},"N":{(4,2),(4,3),(4,5),(4,6)}}
    fichasJugadas2 = {"B":{(4,0)},"N":{(2,4),(3,4),(5,4),(6,4)}}
    
    fichasJugadas3 = {"N":{(4,1),(4,7)},"B":{(4,2),(4,3),(4,5),(4,6)}}
    fichasJugadas4 = {"N":{(4,0)},"B":{(2,4),(3,4),(5,4),(6,4)}}
    
    assert volteadasVerticalmente(fichasJugadas1,(4,4),"B",8) == {(4,2),(4,3),(4,5),(4,6)}
    assert volteadasVerticalmente(fichasJugadas2,(4,4),"B",8) == set()
    
    assert volteadasVerticalmente(fichasJugadas3,(4,4),"N",8) == {(4,2),(4,3),(4,5),(4,6)}
    assert volteadasVerticalmente(fichasJugadas4,(4,4),"N",8) == set()



def test_volteadasDiagonalDescendiente():

    fichasJugadas1 = {"B":{(1,1),(7,7)},"N":{(2,2),(3,3),(5,5),(6,6)}}
    fichasJugadas2 = {"B":{(0,0)},"N":{(2,2),(3,3),(5,5),(6,6)}}
    
    fichasJugadas3 = {"N":{(1,1),(7,7)},"B":{(2,2),(3,3),(5,5),(6,6)}}
    fichasJugadas4 = {"N":{(0,0)},"B":{(2,2),(3,3),(5,5),(6,6)}}
    

    assert volteadasDiagonalDescendiente(fichasJugadas1,(4,4),"B",8) == {(2,2),(3,3),(5,5),(6,6)}
    assert volteadasDiagonalDescendiente(fichasJugadas2,(4,4),"B",8) == set()
    
    assert volteadasDiagonalDescendiente(fichasJugadas3,(4,4),"N",8) == {(2,2),(3,3),(5,5),(6,6)}
    assert volteadasDiagonalDescendiente(fichasJugadas4,(4,4),"N",8) == set()



def test_volteadasDiagonalAscendiente():

    fichasJugadas1 = {"B":{(7,1),(1,7)},"N":{(6,2),(5,3),(3,5),(2,6)}}
    fichasJugadas2 = {"B":{(1,7)},"N":{(7,1),(6,2),(5,3),(3,5)}}
    
    fichasJugadas3 = {"N":{(7,1),(1,7)},"B":{(6,2),(5,3),(3,5),(2,6)}}
    fichasJugadas4 = {"N":{(1,7)},"B":{(7,1),(6,2),(5,3),(3,5)}}

    assert volteadasDiagonalAscendiente(fichasJugadas1,(4,4),"B",8) == {(6,2),(5,3),(3,5),(2,6)}
    assert volteadasDiagonalAscendiente(fichasJugadas2,(4,4),"B",8) == set()
    
    assert volteadasDiagonalAscendiente(fichasJugadas3,(4,4),"N",8) == {(6,2),(5,3),(3,5),(2,6)}
    assert volteadasDiagonalAscendiente(fichasJugadas4,(4,4),"N",8) == set()



def test_turnoOpuesto():

    assert turnoOpuesto("B") == "N"
    assert turnoOpuesto("N") == "B"



def test_normalizarLectura():

    assert normalizarLectura("B5\n") == "B5"
    assert normalizarLectura("N\n") == "N"
    assert normalizarLectura("n5\n") == "N5"
