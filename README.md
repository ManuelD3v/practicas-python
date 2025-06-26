
# Gestor de una biblioteca

Este proyecto es una practica realizada para extrapolar los conocimientos adquiridos en java a python. El fin de este proyecto es adquirir conocimientos necesarios para comenzar con los modelos basicos de inteligencia artificial.  

Para este proyecto son necesarios conceptos básicos de programación, como pueden ser las clases y objetos y subfunciones, como las diferentes estructuras de datos(Arrays y diccionarios).

Este proyecto tiene fines meramente educativos por lo que no esta pensado para que otros usuarios hagan crecer el proyecto, por este motivo unicamente el desarrollador podra actualizar el proyecto según avance el curso.

# Descripcion del sistema

El sistema se encarga de gestionar el stock de una biblioteca implementando las siguientes funciones:

- Agregar libro:
    > Pide al usuario el titulo del libro, el autor y el numero de ejemplares. El sistema asigna automaticamente un isbn unico al libro.

- Buscar por titulo:
    > Dado un titulo muestra todos los libros con ese nombre.

- Buscar por autor: 
    > Dado un autor muestra todos los libros del mismo.

- Prestar libro:
    > Dado un isbn resta uno a la cantidad de ejemplares en la biblioteca.

- Devolver libro:
    > Dado un isbn aumenta en uno la cantidad de ejemplares en la biblioteca.

- Mostrar Libros:
    > Muestra todos los libros de la biblioteca.

- Guardar Biblioteca:
    > Dado un nombre crea un Json con el contenidio de la biblioteca.

- Cargar Biblioteca:
    > Dado un nombre carga una bibliotece de un archivo Json.

# Ejecución de test

Una vez abierta la terminal escribiendo `pytest` se ejecutaran los test de forma automatica.

# Cargar/Guardar bibliotecas

Primero pasamos todos los libros a diccionarios y creamos un diccionario de libros diccionario para poder crear un archivo tipo json.

A la hora de cargar la biblioteca tenemos que hacerlo a la inversa, una vez tenemos la biblioteca con libros diccionario tenemos que pasarlos a libros normales.
