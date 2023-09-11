import uuid
import os
import yaml


def generar_id():
    return str(uuid.uuid4().int)[:6]


def crear_id_unica():
    """
    Checar si el id ya existe
    Si existe, crear otro
    Si no existe, retornar el id
    """

    data_file = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'data',
                             'peliculas_data.yml')

    if not os.path.exists(data_file):
        pass

    with open(data_file, 'r') as archivo:
        data = yaml.load(archivo, Loader=yaml.FullLoader)

    try:
        while True:
            id_gen = generar_id()
            if id_gen not in data['peliculas']:
                return id_gen
    except TypeError:  # Caution
        return generar_id()  # Si no hay peliculas, retornar un id


class Pelicula:
    nombre = ""
    genero = ""
    duracion = ""
    clasificacion = ""
    idioma = ""
    subtitulos = ""
    sinopsis = ""
    director = ""
    actores = ""
    productora = ""
    pais = ""
    anio = ""

    def __init__(self, nombre, genero, duracion, clasificacion, idioma, subtitulos, sinopsis, director, actores,
                 productora, pais, anio):
        self.id = crear_id_unica()
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.idioma = idioma
        self.subtitulos = subtitulos
        self.sinopsis = sinopsis
        self.director = director
        self.actores = actores
        self.productora = productora
        self.pais = pais
        self.anio = anio
