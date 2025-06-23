from libro import Libro
import orjson
from excepcionCustom import ExcepcionCustom
    
class Biblioteca:

    def __init__(self):
        self.estanteria = {}

    def agregar_libro(self,libro : Libro):

        self.estanteria[libro.isbn] = libro

    def buscar_por_titulo(self,titulo : str):
        if titulo.isalnum:
            raise ExcepcionCustom("Titulo no alpha-numerico", 100)
        
        if titulo == "":
            raise ExcepcionCustom("Titulo vacio", 101)

        paquete = []

        for x in self.estanteria.values():
            if x.titulo == titulo:
                paquete.append(x)
        
        return paquete
    
    def buscar_por_autor(self,autor : str):
        if autor.isalnum:
            raise ExcepcionCustom("Autor no alpha-numerico", 200)
        
        if autor == "":
            raise ExcepcionCustom("Autor vacio", 201)

        paquete = []

        for x in self.estanteria.values():
            if x.autor == autor:
                paquete.append(x)
        
        return paquete
    
    def prestar_libro(self, isbn : str):

        if isbn.isalnum:
            raise ExcepcionCustom("Isbn no alpha-numerico", 300)
        
        if isbn == "":
            raise ExcepcionCustom("Isbn vacio", 301)
        
        for x in isbn:
            if x == " ":
                raise ExcepcionCustom("Isbn contiene espacio", 302)

        for x in self.estanteria:

            if x == isbn:
                if self.estanteria[x].ejemplares_disponibles > 0:
                    self.estanteria[x].ejemplares_disponibles -= 1
                    return True
                else:
                    return False

    def devolver_libro(self, isbn : str):

        for x in self.estanteria:
            if x == isbn:
                self.estanteria[x].ejemplares_disponibles += 1
                return True
        
        return False
    
    def listar_libros(self):
        indice = 1
        for x in self.estanteria.values():
            print ("___________________________")
            print (f"Libro numero {indice}")
            print ("___________________________")
            print (x)
            indice += 1

    def guardar(self, filename):
        path = filename+".json"

        datos = {}

        for isbn,libro in self.estanteria.items():
            datos[isbn] = libro.to_dict()

        with open(path,"wb") as archivo:
            archivo.write(orjson.dumps(datos,option=orjson.OPT_INDENT_2))

    def cargar(self, filename):
        path = filename + ".json"
        with open(path, "rb") as archivo:
            datos = orjson.loads(archivo.read())
        
        for isbn,libro in datos.items():
            self.estanteria [isbn] = Libro.from_dict(libro)

    def validar_isbn
