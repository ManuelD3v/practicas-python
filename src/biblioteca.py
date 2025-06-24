from libro import Libro
import orjson
from excepcionCustom import ExcepcionCustom
    
class Biblioteca:

    def __init__(self):
        self.estanteria = {}

    def validar_titulo(titulo : str):

        if titulo == None:

            raise ExcepcionCustom("Titulo vacio",100)
        
        if not titulo.isalnum:

            raise ExcepcionCustom("Titulo no alpha-numerico", 101) 
    
    def validar_autor(autor : str):

        if autor == None:

            raise ExcepcionCustom("Autor vacio", 200)
        
        if not autor.isalnum:

            raise ExcepcionCustom("Autor no alpha-numerico", 201)

    def validar_isbn(isbn : str):

        if isbn == None:
            
            raise ExcepcionCustom("Isbn vacio", 300)
        
        if not isbn.isalnum:

            raise ExcepcionCustom("Isbn no alpha-numerico", 301)
      
    def validar_ejemplares(ejemplares : str):

        if ejemplares == None:
            
            raise ExcepcionCustom("Ejemplares vacio", 400)

        if not ejemplares.isdecimal:
            
            raise ExcepcionCustom("Ejemplares no es decimal", 401)
        
        if int(ejemplares) < 0:

            raise ExcepcionCustom("Numero de ejemplares negativo", 403)
        
    def validar_filename(filename : str):

        if filename == None:

            raise ExcepcionCustom("Nombre de archivo vacio", 500)
        
        if not filename.isalnum:

            raise ExcepcionCustom("Nombre de archivo no alpha-numerico", 501)

    def agregar_libro(self,libro : Libro):

        self.estanteria[libro.isbn] = libro

    def buscar_por_titulo(self,titulo : str):

        Biblioteca.validar_titulo(titulo)
        
        paquete = []

        for x in self.estanteria.values():

            if x.titulo == titulo:

                paquete.append(x)
        
        return paquete
    
    def buscar_por_autor(self,autor : str):

        Biblioteca.validar_autor(autor)

        paquete = []

        for x in self.estanteria.values():

            if x.autor == autor:

                paquete.append(x)
        
        return paquete
    
    def prestar_libro(self, isbn : str):

        Biblioteca.validar_isbn(isbn)

        for x in self.estanteria:

            if x == isbn:

                if self.estanteria[x].ejemplares_disponibles > 0:

                    self.estanteria[x].ejemplares_disponibles -= 1

                    return True
                
                else:

                    return False

    def devolver_libro(self, isbn : str):

        Biblioteca.validar_isbn(isbn)

        for x in self.estanteria:

            if x == isbn:

                self.estanteria[x].ejemplares_disponibles += 1

                return True
        
        return False
    
    def listar_libros(self):

        if self.estanteria.__len__() == 0:
            raise ExcepcionCustom("Biblioteca vacia", 501)

        indice = 1

        for x in self.estanteria.values():

            print ("___________________________")
            print (f"Libro numero {indice}")
            print ("___________________________")
            print (x)

            indice += 1
        
        print ("___________________________")

    def guardar(self, filename):

        Biblioteca.validar_filename(filename)
        
        path = filename+".json"

        datos = {}

        for isbn,libro in self.estanteria.items():

            datos[isbn] = libro.to_dict()

        with open(path,"wb") as archivo:

            archivo.write(orjson.dumps(datos,option=orjson.OPT_INDENT_2))

    def cargar(self, filename):

        Biblioteca.validar_filename(filename)

        path = filename + ".json"

        with open(path, "rb") as archivo:

            datos = orjson.loads(archivo.read())
        
        for isbn,libro in datos.items():
            
            self.estanteria [isbn] = Libro.from_dict(libro)
