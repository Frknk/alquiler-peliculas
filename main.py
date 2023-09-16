from modulos.pelicula import Pelicula
from modulos.cliente import Cliente
import rich
from rich import box
from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table

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


def generar_tabla_rich(objeto):
    tabla = Table(show_edge=True, show_header=False, box=box.MINIMAL)
    for key, value in objeto.__dict__.items():
        if key != 'nombre':
            tabla.add_row(f"[magenta bold] {key.capitalize()}", value)
    return Columns([Panel(tabla, title=objeto.nombre)], equal=True)


# Mostrar datos de pelicula
rconsole = rich.get_console()
tabla_test = generar_tabla_rich(cliente)
rconsole.print(tabla_test, justify="center")
