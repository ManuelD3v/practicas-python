import pytest
from biblioteca import Biblioteca

"""
clases equivalencia autor

clases validas:  
    V1: autor alfanumerico            

clases invalidas:
    I1: autor vacio
    I2: autor con caracteres no alfanumericos
"""

@pytest.mark.parametrize(
    "autor,esperado,clase_equivalencia",
    [
        ("Aladin",True,"V1: autor alfanumerico"),
        ("",False,"I1: autor vacio"),
        ("loco------``````",False,"I2: autor con caracteres no alfanumericos")
    ]
)

def test_autor_valido(autor,esperado : bool, clase_equivalencia: str):
    resultado = Biblioteca.is_author_valid(autor)
    assert resultado == esperado , f"Fallo en clase: {clase_equivalencia}"






