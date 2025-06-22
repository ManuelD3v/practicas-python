from libro import Libro
import orjson
    
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
        with open(path,"wb") as archivo:
            archivo.write(orjson.dumps(self.estanteria))

    def cargar(self, filename):
        path = filename + ".json"
        with open(path, "rb") as archivo:
            self.estanteria = orjson.loads(archivo.read())
        
        print(self.estanteria)
