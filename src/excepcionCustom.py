class ExcepcionCustom(Exception):
    def __init__(self, mensaje : str , codigo : int):
        self.codigo = codigo
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def __str__(self):
        return f"{self.mensaje} (Error codigo: {self.codigo}))"
