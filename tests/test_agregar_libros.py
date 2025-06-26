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

"""
clases equivalencia numero de ejemplares

clases validas:  
    V1: numero de ejemplares de tipo numerico y numero >= 0

clases invalidas:
    I1: numero de ejemplares vacio
    I2: numero de ejemplares con simbolos no numericos
    I3: numero de ejemplares negativo 
"""

@pytest.mark.parametrize(
    "ejemplares,esperado,clase_equivalencia",
    [
        ("123",True,"V1: numero de ejemplares de tipo numerico"),
        ("",False,"I1: numero de ejemplares vacio"),
        ("123@",False,"I2: numero de ejemplares con simbolos no numericos"),
        ("-123",False,"I3: numero de ejemplares negativo"),
    ]
)

def test_numero_ejemplares_valido(ejemplares,esperado : bool, clase_equivalencia: str):
    resultado = Biblioteca.is_stock_valid(ejemplares)
    assert resultado == esperado , f"Fallo en clase: {clase_equivalencia}"

"""
clases equivalencia nombre del archivo

clases validas:  
    V1: nombre del archivo alfanumerico            

clases invalidas:
    I1: nombre del archivo vacio
    I2: nombre del archivo con caracteres no alfanumericos
"""

@pytest.mark.parametrize(
    "filename,esperado,clase_equivalencia",
    [
        ("123aaa",True,"V1: nombre del archivo alfanumerico"),
        ("",False,"I1: nombre del archivo vacio"),
        ("123@",False,"I2: nombre del archivo con caracteres no alfanumericos")
    ]
)

def test_nombre_archivo_valido(filename,esperado : bool, clase_equivalencia: str):
    resultado = Biblioteca.is_filename_valid(filename)
    assert resultado == esperado , f"Fallo en clase: {clase_equivalencia}"
