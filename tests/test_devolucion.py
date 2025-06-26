import pytest
from biblioteca import Biblioteca
"""
clases equivalencia isbn

clases validas:  
    V1: isbn numerico > 0            

clases invalidas:
    I1: isbn vacio
    I2: isbn con caracteres no numericos
    I3: isbn < 0
"""

@pytest.mark.parametrize(
    "isbn,esperado,clase_equivalencia",
    [
        ("1",True,"V1: isbn numerico"),
        ("",False,"I1: isbn vacio"),
        ("123@",False,"I2: isbn con caracteres no numericos"),
        ("-1",False,"I3: isbn < 0")
    ]
)

def test_isbn_valido(isbn,esperado : bool, clase_equivalencia: str):
    resultado = Biblioteca.is_isbn_valid(isbn)
    assert resultado == esperado , f"Fallo en clase: {clase_equivalencia}"
