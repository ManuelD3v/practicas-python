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

def ask_book(biblioteca : Biblioteca):
    
    try:
    
        title = input("Titulo: ")

        if not Biblioteca.is_title_valid(title):
            raise ExcepcionCustom("Titulo invalido.")

        author = input("Autor: ")

        if not Biblioteca.is_author_valid(author):
            raise ExcepcionCustom("Autor invalido.")

        stock = input("Numero de ejemplares disponibles: ")

        if not Biblioteca.is_stock_valid(stock):
            raise ExcepcionCustom("Stock invalido.")
        
        stock = int(stock)

        biblioteca.add_book(title,author,stock)
    
    except ExcepcionCustom as e:
        print(f"Error encontrado: {e}")

def ask_title(biblioteca : Biblioteca):

    title = input("Titulo: ")

    try:

        if not Biblioteca.is_title_valid(title):
            raise ExcepcionCustom("Titulo invalido.")

        books = biblioteca.search_by_title(title)

        if books.__len__ == 0:

            print("No hay libros con ese titulo")

        else:

            for x in books:

                print(x)

    except ExcepcionCustom as e:
        print(f"Error encontrado: {e}")
    
def ask_author(biblioteca : Biblioteca):

    author = input("Autor: ")

    try:

        if not Biblioteca.is_author_valid(author):
            raise ExcepcionCustom("Autor invalido.")

        books = biblioteca.search_by_author(author)

        if books.__len__ == 0:

            print("No hay libros con ese autor")
        
        else:

            for x in books:

                print(x)

    except ExcepcionCustom as e:
        print(f"Error encontrado: {e}")

    

def lend_book(biblioteca : Biblioteca):

    isbn = input("Dame el isbn del libro: ")

    try:
        if not Biblioteca.is_isbn_valid(isbn):
            raise ExcepcionCustom("Isbn invalido.")

        if biblioteca.lend_book(int(isbn)):

            print("Prestamo exitoso")

        else:

            print("Prestamo fallido")

    except ExcepcionCustom as e:
        print(f"Error encontrado: {e}")

def return_book(biblioteca : Biblioteca):

    isbn = input("Dame el isbn del libro: ")
    
    try:

        if not Biblioteca.is_isbn_valid(isbn):
            raise ExcepcionCustom("Isbn invalido.")

        if biblioteca.return_book(isbn):

            print("Devolucion exitosa")
        
        else:

            print("Libro no encontrado")

    except ExcepcionCustom as e:
        print(f"Error encontrado. {e}")

def save_bookshelf(biblioteca : Biblioteca):

    filename = input("Dime el nombre del archivo a guardar: ")

    try:

        if not Biblioteca.is_filename_valid(filename):
            raise ExcepcionCustom("Ruta invalida.")

        biblioteca.save(filename)

    except ExcepcionCustom as e:
        print(f"Error encontrado: {e}")


def load_bookshelf(biblioteca : Biblioteca):

    filename = input("Dime el nombre del archivo a cargar: ")

    try:

        if not Biblioteca.is_filename_valid(filename):
            raise ExcepcionCustom("Ruta invalida.")

        biblioteca.load(filename)

    except ExcepcionCustom as e:
        print(f"Error encontrado: {e}")

    except FileNotFoundError as e:
        print(f"No existe fichero con el nombre de {filename}")

if __name__ == "__main__":

    biblioteca = Biblioteca()

    opcion : int
    opcion = None

    while (opcion != 9):
        
        menu()
        opcion = int(input("Seleccion: "))

        match opcion:
            case 1 : ask_book(biblioteca) 

            case 2 : ask_title(biblioteca)

            case 3 : ask_author(biblioteca)

            case 4 : lend_book(biblioteca)

            case 5 : return_book(biblioteca)

            case 6: 
                
                try:
                    biblioteca.show_books()
                except ExcepcionCustom as e:
                    print(f"Error encontrado: {e}")

            case 7: save_bookshelf(biblioteca)

            case 8: load_bookshelf(biblioteca)
            
            case 9: print("Saliendo")

            case _: print("Opcion fuera de rango")
        
        bin = input("Pulsa enter para continuar.")

        limpiar_pantalla()
