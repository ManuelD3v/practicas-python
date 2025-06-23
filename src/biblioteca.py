from libro import Libro
import orjson,json
    
class Biblioteca:

    def __init__(self):
        self.estanteria = {}

    def agregar_libro(self,libro : Libro):

        self.estanteria[libro.isbn] = libro

    def buscar_por_titulo(self,titulo : str):
        paquete = []

        for x in self.estanteria.values():
            if x.titulo == titulo:
                paquete.append(x)
        
        return paquete
    
    def buscar_por_autor(self,autor : str):
        paquete = []

        for x in self.estanteria.values():
            if x.autor == autor:
                paquete.append(x)
        
        return paquete
    
    def prestar_libro(self, isbn : str):

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
