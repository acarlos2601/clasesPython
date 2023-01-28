def texto_split(caracter:str =" "):
    try:
        return texto.split(caracter)
    except:
        return f'Error. Ingrese un caracter valido de separacion.'

def texto_joined(caracter:str, lista:list):
    return caracter.join(lista)

def texto_count(caracter:str = " "):
    try:
        return texto.count(caracter)
    except:
        return f'Error. Ingrese un caracter valido de separacion.'

def texto_find(caracter):
    try:
        return texto.find(caracter)
    except:
        return f'Error. Ingrese un caracter valido de separacion.'

def texto_upperCase():
    return texto.upper()

def texto_lower():
    return texto.lower()

texto = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen."