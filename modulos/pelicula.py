import uuid

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

    def __init__(self, nombre, genero, duracion, clasificacion, idioma, subtitulos, sinopsis, director, actores, productora, pais, anio):
        self.id = str(uuid.uuid4().int)[:4]
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
        