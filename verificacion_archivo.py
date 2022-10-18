#Correcta lectura del arhivo 

def ingresaArchivo():
    """
    ingresaArchivo :: None -> File

    . Chequea que el archivo el archivo existe. Devuelve el archivo abierto a la funcion main.
    """
    
    nombreArchivo = input("Introduzca el archivo de jugadas: ")
    archivoEnExtension = nombreArchivo + '.txt'
    
    while not chequeaArchivo(archivoEnExtension): # SI NO SE ENCUENTRA EL ARCHIVO, REINTENTA.
        nombreArchivo = input("Introduzca el archivo de jugadas: ")
        archivoEnExtension = nombreArchivo + '.txt'
    
    archivo = open(archivoEnExtension)
    
    return archivo
    

def chequeaArchivo(archivoEnExtension):
    """
    chequeaArchivo :: string -> bool

    . Chequea que el archivo exista en el directorio. Si existe, devuelve true, sino devuelve false.
    """

    try: 
        archivoExiste = open(archivoEnExtension)
        archivoExiste.close()

    except:
        print('\nEl archivo no ha sido encontrado. ')
        return False
        
    else: 
        return True
    
