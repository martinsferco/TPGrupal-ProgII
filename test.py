#Test de todas las funciones

from tablero import inicializarTablero


def test_inicializarTablero():

    assert inicializarTablero() == [["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","B","N","","",""],
                                    ["","","","N","B","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""]]
