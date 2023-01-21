biblioteca= {
    'drama': [
        {'titulo': 'Libro drama 1', 'autor': 'Autor 1', 'prestado': False},
        {'titulo': 'Libro drama 2', 'autor': 'Autor 2', 'prestado': True}
    ],
    'comedia': [
        {'titulo': 'Novela comedia 1', 'autor': 'Autor 3', 'prestado': False},
        {'titulo': 'Libro comedia 2', 'autor': 'Autor 4', 'prestado': True}
    ]
}

usuarios= ['Carlos', 'Jose', 'Maria', 'Ana']

def get_categorias():
    return list(biblioteca.keys())

def get_libros():
    libros = []
    for categoria in biblioteca.values():
        for libro in categoria:
            libros.append((libro['titulo'], libro['autor']))
    return libros

def change_estadoLibro(titulo, estado):
    for categorias in biblioteca.values():
        for libro in categorias:
            if libro['titulo'] == titulo:
                libro['prestado'] = estado
                print("El estado del libro ",titulo," ha sido cambiado a prestado")
                return libro
    return "No se ha encontrado el libro"

def get_usuarios():
    return usuarios

print("Funcion 1 - Obtener la lista de categorías de libros :")
print(get_categorias())
print("\nFuncion 2 - Obtener nombres de los libros y autores :")
print(get_libros())
print("\nFuncion 3 - Poder cambiar el estado de un libro a prestado :")
print(change_estadoLibro('Libro drama 2',True))
print("\nFuncion 4 -  Lista de usuarios de la biblioteca :")
print(get_usuarios())