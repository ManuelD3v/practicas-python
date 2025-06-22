from biblioteca import Biblioteca
from libro import Libro

def menu():
    print(" Menu ")
    print("1. Agregar libro")
    print("2. Buscar por titulo")
    print("3. Buscar por autor")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Lista de libros")
    print("7. Salir")

def pedir_libro(biblioteca : Biblioteca):
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    isbn = input("Isbn: ")
    ejemplares = int(input("Numero de ejemplares disponibles: "))

    libro : Libro

    libro = Libro(titulo, autor, isbn, ejemplares)

    biblioteca.agregar_libro(libro)

def pedir_titulo(biblioteca : Biblioteca):
    titulo = input("Titulo: ")

    libros = biblioteca.buscar_por_titulo(titulo)
    if libros.__len__ == 0:
        print("No hay libros con ese titulo")
    else:
        for x in libros:
            print(x)
    
def pedir_autor(biblioteca : Biblioteca):
    autor = input("Autor: ")

    libros = biblioteca.buscar_por_autor(autor)
    if libros.__len__ == 0:
        print("No hay libros con ese autor")
    else:
        for x in libros:
            print(x)

def prestar_libro(biblioteca : Biblioteca):
    isbn = input("Dame el isbn del libro: ")

    if biblioteca.prestar_libro(isbn):
        print("Prestamo exitoso")
    else:
        print("Prestamo fallido")

def devolver_libro(biblioteca : Biblioteca):
    isbn = input("Dame el isbn del libro: ")

    if biblioteca.devolver_libro(isbn):
        print("Devolucion exitosa")
    
    else:
        print("Devolucion fallida")

if __name__ == "__main__":

    biblioteca = Biblioteca()

    opcion : int
    opcion = None
    while (opcion != 7):
        
        menu()
        opcion = int(input("Seleccion: "))

        match opcion:
            case 1 : pedir_libro(biblioteca) 

            case 2 : pedir_titulo(biblioteca)

            case 3 : pedir_autor(biblioteca)

            case 4 : prestar_libro(biblioteca)

            case 5 : devolver_libro(biblioteca)

            case 6: biblioteca.listar_libros()
