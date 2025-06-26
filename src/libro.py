class Libro:

    def __init__(self, title : str, author : str, isbn : int, stock : int):

        self.title = title
        self.author = author
        self.isbn = isbn
        self.stock = stock

    def __str__(self):

        libro = ""
        libro += f"titulo: {self.title} \n"
        libro += f"autor: {self.author} \n"
        libro += f"ISBN: {self.isbn} \n"
        libro += f"ejemplares disponibles: {self.stock}"

        return libro

    def to_dict(self):
        
        return {
            "titulo" : self.title,
            "autor" : self.author,
            "isbn" : self.isbn,
            "ejemplares disponibles" : self.stock
        }
    
    def from_dict(data : dict):
        
        title = data["titulo"]
        author = data["autor"]
        isbn = data["isbn"]
        stock = data["ejemplares disponibles"]

        return Libro(title,author,isbn,stock)
