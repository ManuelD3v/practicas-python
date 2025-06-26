from libro import Libro
from idGenerator import IDGenerator
import orjson
from excepcionCustom import ExcepcionCustom
    
class Biblioteca:

    def __init__(self):
        self.bookshelf = {}
        self.genId = IDGenerator()

    @staticmethod 
    def is_title_valid(title : str):
        
        return title.isalnum()

    @staticmethod     
    def is_author_valid(author : str):
        
        return author.isalnum()

    @staticmethod 
    def is_isbn_valid(isbn : str):

        return isbn.isdecimal()

    @staticmethod   
    def is_stock_valid(stock : str):

        if not stock.isdecimal():
            
            return False
        
        return int(stock) > 0

    @staticmethod    
    def is_filename_valid(filename : str):
        
        return filename.isalnum()
    
    @staticmethod
    def is_bookshelf_valid(bookshelf : dict):
        
        return bookshelf.__len__ != 0

    def add_book(self,title : str ,author : str, stock :int):

        book : Libro

        book = Libro(title,author,str(self.genId.next_id()), stock)

        self.bookshelf[book.isbn] = book

    def search_by_title(self,title : str):

        paquete = []

        for x in self.bookshelf.values():

            if x.title == title:

                paquete.append(x)
        
        return paquete
        
        
    
    def search_by_author(self,author : str):

        paquete = []

        for x in self.bookshelf.values():

            if x.author == author:

                paquete.append(x)
        
        return paquete
    
    def lend_book(self, isbn : int):


        for x in self.bookshelf:

            if x == isbn:

                self.bookshelf[x].stock -= 1

                return True
            
        return False

    def return_book(self, isbn : str):

        for x in self.bookshelf:

            if x == isbn:

                self.bookshelf[x].stock += 1

                return True
        
        return False
        
    def show_books(self):

        indx = 1

        for x in self.bookshelf.values():

            print ("___________________________")
            print (f"Libro numero {indx}")
            print ("___________________________")
            print (x)

            indx += 1
        
        print ("___________________________")

    def save(self, filename):
        
        path = filename+".json"

        data = {}

        for isbn,libro in self.bookshelf.items():

            data[isbn] = libro.to_dict()

        with open(path,"wb") as archivo:

            archivo.write(orjson.dumps(data,option=orjson.OPT_INDENT_2))

    def load(self, filename):

        path = filename + ".json"

        with open(path, "rb") as archivo:

            data = orjson.loads(archivo.read())
        
        self.genId.reset()

        for isbn,libro in data.items():
            self.genId.next_id()
            self.bookshelf [isbn] = Libro.from_dict(libro)
