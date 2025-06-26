import pytest
from biblioteca import Biblioteca

"""
clases equivalencia titulo

clases validas:  
    V1: titulo alfanumerico            

clases invalidas:
    I1: titulo vacio
    I2: titulo con caracteres no alfanumericos
"""
@pytest.mark.parametrize(
    "titulo,esperado,clase_equivalencia",
    [
        ("Aladin",True,"V1: titulo alfanumerico"),
        ("",False,"I1: titulo vacio"),
        ("loco------``````",False,"I2: titulo con caracteres no alfanumerico")
    ]
)

def test_titulo_valido(titulo,esperado : bool, clase_equivalencia: str):
    resultado = Biblioteca.is_title_valid(titulo)
    assert resultado == esperado , f"Fallo en clase: {clase_equivalencia}"
