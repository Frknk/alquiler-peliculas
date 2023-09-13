from modulos.pelicula import Pelicula
from modulos.cliente import Cliente
import os

pelicula = Pelicula(
    nombre="El señor de los anillos",
    genero="Fantasia",
    duracion="120",
    clasificacion="B",
    idioma="Ingles",
    subtitulos="Español",
    sinopsis="Un hobbit tiene que destruir un anillo",
    director="Peter Jackson",
    actores="Elijah Wood, Ian McKellen, Viggo Mortensen",  # [Elijah Wood, Ian McKellen, Viggo Mortensen] Lista
    productora="New Line Cinema",
    pais="Estados Unidos",
    fecha="2001",
)

cliente = Cliente(
    nombre="Juan",
    apellido="Perez",
    dni="12345678",
    direccion="Av. Siempre Viva 123",
    telefono="123456789",
    email="juan@email.com",
    password="123456",
)


print(pelicula.getdata_str())
print(os.getcwd())
my_string = "This is a backslash: \\"
print(my_string)
print(cliente.getdata_str())
print(cliente.getdata())
