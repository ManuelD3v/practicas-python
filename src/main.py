from biblioteca import Biblioteca
from libro import Libro
from excepcionCustom import ExcepcionCustom

def menu():

    print(" Menu ")
    print("1. Agregar libro")
    print("2. Buscar por titulo")
    print("3. Buscar por autor")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Lista de libros")
    print("7. Guardar estanteria")
    print("8. Cargar estanteria")
    print("9. Salir")

def limpiar_pantalla():

    x = 0

    while x < 13:

        print("")

        x += 1

def pedir_libro(biblioteca : Biblioteca):
    try:

        titulo = input("Titulo: ")
        Biblioteca.validar_titulo(titulo)

        autor = input("Autor: ")
        Biblioteca.validar_autor(autor)

        isbn = input("Isbn: ")
        Biblioteca.validar_isbn(isbn)

        ejemplares = int(input("Numero de ejemplares disponibles: "))
        Biblioteca.validar_ejemplares(ejemplares)

        libro : Libro

        libro = Libro(titulo, autor, isbn, ejemplares)

        try:
            
            biblioteca.agregar_libro(libro)

        except ExcepcionCustom as e:
            print(f"Error encontrado: {e}")
    
    except ExcepcionCustom as e:
        print(f"Error encontrado: {e}")

def pedir_titulo(biblioteca : Biblioteca):

    titulo = input("Titulo: ")

    try:

        libros = biblioteca.buscar_por_titulo(titulo)

    except ExcepcionCustom as e:
        print(f"Error encontrado: {e}")

    if libros.__len__ == 0:

        print("No hay libros con ese titulo")

    else:

        for x in libros:

            print(x)
    
def pedir_autor(biblioteca : Biblioteca):

    autor = input("Autor: ")

    try:

        libros = biblioteca.buscar_por_autor(autor)
    
    except ExcepcionCustom as e:
        print(f"Error encontrado: {e}")

    if libros.__len__ == 0:

        print("No hay libros con ese autor")
        
    else:

        for x in libros:

            print(x)

def prestar_libro(biblioteca : Biblioteca):

    isbn = input("Dame el isbn del libro: ")

    try:

        if biblioteca.prestar_libro(isbn):

            print("Prestamo exitoso")

        else:

            print("Prestamo fallido")

    except ExcepcionCustom as e:
        print(f"Error encontrado: {e}")

def devolver_libro(biblioteca : Biblioteca):

    isbn = input("Dame el isbn del libro: ")


    try:
        if biblioteca.devolver_libro(isbn):

            print("Devolucion exitosa")
        
        else:

            print("Libro no encontrado")

    except ExcepcionCustom as e:
        print(f"Error encontrado: {e}")

def guardar_estanteria(biblioteca : Biblioteca):

    filename = input("Dime el nombre del archivo a guardar: ")

    try:
        biblioteca.guardar(filename)
    except ExcepcionCustom as e:
        print(f"Error encontrado: {e}")


def cargar_estanteria(biblioteca : Biblioteca):

    filename = input("Dime el nombre del archivo a cargar: ")

    try:
        biblioteca.cargar(filename)
    except ExcepcionCustom as e:
        print(f"Error encontrado: {e}")


if __name__ == "__main__":

    biblioteca = Biblioteca()

    opcion : int
    opcion = None

    while (opcion != 9):
        
        menu()
        opcion = int(input("Seleccion: "))

        match opcion:
            case 1 : pedir_libro(biblioteca) 

            case 2 : pedir_titulo(biblioteca)

            case 3 : pedir_autor(biblioteca)

            case 4 : prestar_libro(biblioteca)

            case 5 : devolver_libro(biblioteca)

            case 6: 
                
                try:
                    biblioteca.listar_libros()
                except ExcepcionCustom as e:
                    print(f"Error encontrado: {e}")

            case 7: guardar_estanteria(biblioteca)

            case 8: cargar_estanteria(biblioteca)
        
        bin = input("Pulsa enter para continuar.")

        limpiar_pantalla()
