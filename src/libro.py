class Libro:

    def __init__(self, titulo : str, autor : str, isbn : str, ejemplares_disponibles : int):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ejemplares_disponibles = ejemplares_disponibles

    def __str__(self):
        libro += f"titulo: {self.titulo} \n"
        libro += f"autor: {self.autor} \n"
        libro += f"ISBN: {self.isbn} \n"
        libro += f"ejemplares disponibles: {self.ejemplares_disponibles}"

        return libro