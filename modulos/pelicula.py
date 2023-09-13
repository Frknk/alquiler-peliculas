"""
@Frknk

Clases:
    - Pelicula

Atributos:
    None

Funciones:
    - Pelicula() : Constructor de la clase Pelicula, ejecutara automaticamente la funcion crear_id_unica() para generar
      un id unico para la pelicula.

"""
from gestor_id import GestorID


class Pelicula:
    """
    Clase para representar una pelicula

    ...

    Atributos
    ---------
    id : str
        identificador unico de la pelicula, creado automaticamente
        formato: 6 caracteres alfanumericos
    nombre : str
        nombre de la pelicula
    genero : str
        genero de la pelicula - formato: genero1, genero2, genero3
    duracion : str
        duracion de la pelicula - formato: hh:mm
    clasificacion : str
        clasificacion de la pelicula - formato: A, AA, B, B15, C, D
    idioma : str
        idioma de la pelicula
    subtitulos : str
        subtitulos de la pelicula
    sinopsis : str
        breve resumen de la pelicula
    director : str
        director de la pelicula
    actores : str
        actores de la pelicula - formato: actor1, actor2, actor3
    productora : str
        productora de la pelicula
    pais : str
        pais origen de la pelicula
    fecha : str
        fecha de estreno de la pelicula - formato: dd/mm/aaaa

    Metodos
    -------
    getid()
        Obtener id de la pelicula
    getnombre()
        Obtener nombre de la pelicula
    getgenero()
        Obtener genero de la pelicula
    getduracion()
        Obtener duracion de la pelicula
    getclasificacion()
        Obtener clasificacion de la pelicula
    getidioma()
        Obtener idioma de la pelicula
    getsubtitulos()
        Obtener subtitulos de la pelicula
    getsinopsis()
        Obtener sinopsis de la pelicula
    getdirector()
        Obtener director de la pelicula
    getactores()
        Obtener actores de la pelicula
    getproductora()
        Obtener productora de la pelicula
    getpais()
        Obtener pais de la pelicula
    getfecha()
        Obtener fecha de la pelicula
    setnombre(nombre)
        Cambiar nombre de la pelicula
    setgenero(genero)
        Cambiar genero de la pelicula
    setduracion(duracion)
        Cambiar duracion de la pelicula
    setclasificacion(clasificacion)
        Cambiar clasificacion de la pelicula
    setidioma(idioma)
        Cambiar idioma de la pelicula
    setsubtitulos(subtitulos)
        Cambiar subtitulos de la pelicula
    setsinopsis(sinopsis)
        Cambiar sinopsis de la pelicula
    setdirector(director)
        Cambiar director de la pelicula
    setactores(actores)
        Cambiar actores de la pelicula
    setproductora(productora)
        Cambiar productora de la pelicula
    setpais(pais)
        Cambiar pais de la pelicula
    setfecha(fecha)
        Cambiar fecha de la pelicula
    getdata()
        Obtener datos de la pelicula
    __str__()
        Obtener representacion en string de la pelicula
    """

    def __init__(
        self,
        nombre: str,
        genero: str,
        duracion: str,
        clasificacion: str,
        idioma: str,
        subtitulos: str,
        sinopsis: str,
        director: str,
        actores: str,
        productora: str,
        pais: str,
        fecha: str,
    ):
        """
        Constructor de la clase Pelicula

        Parametros
        ----------
        nombre : str
            nombre de la pelicula
        genero : str
            genero de la pelicula - formato: genero1, genero2, genero3
        duracion : str
            duracion de la pelicula - formato: hh:mm
        clasificacion : str
            clasificacion de la pelicula - formato: A, AA, B, B15, C, D
        idioma : str
            idioma de la pelicula
        subtitulos : str
            subtitulos de la pelicula
        sinopsis : str
            breve resumen de la pelicula
        director : str
            director de la pelicula
        actores : str
            actores de la pelicula - formato: actor1, actor2, actor3
        productora : str
            productora de la pelicula
        pais : str
            pais origen de la pelicula
        fecha : str
            fecha de estreno de la pelicula - formato: dd/mm/aaaa
        """
        self.id = GestorID.crear_id_unica("../data/peliculas_data.yml")
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
        self.fecha = fecha

    def getid(self) -> str:
        """
        Obtener id de la pelicula

        Return
        ------
        id : str
            identificador unico de la pelicula
        """
        return self.id

    def getnombre(self) -> str:
        """
        Obtener nombre de la pelicula

        Return
        ------
        nombre : str
            nombre de la pelicula
        """
        return self.nombre

    def getgenero(self) -> str:
        """
        Obtener genero de la pelicula

        Return
        ------
        genero : str
            genero de la pelicula
        """
        return self.genero

    def getduracion(self) -> str:
        """
        Obtener duracion de la pelicula

        Return
        ------
        duracion : str
            duracion de la pelicula
        """
        return self.duracion

    def getclasificacion(self) -> str:
        """
        Obtener clasificacion de la pelicula

        Return
        ------
        clasificacion : str
            clasificacion de la pelicula
        """
        return self.clasificacion

    def getidioma(self) -> str:
        """
        Obtener idioma de la pelicula

        Return
        ------
        idioma : str
            idioma de la pelicula
        """
        return self.idioma

    def getsubtitulos(self) -> str:
        """
        Obtener subtitulos de la pelicula

        Return
        ------
        subtitulos : str
            subtitulos de la pelicula
        """
        return self.subtitulos

    def getsinopsis(self) -> str:
        """
        Obtener sinopsis de la pelicula

        Return
        ------
        sinopsis : str
            sinopsis de la pelicula
        """
        return self.sinopsis

    def getdirector(self) -> str:
        """
        Obtener director de la pelicula

        Return
        ------
        director : str
            director de la pelicula
        """
        return self.director

    def getactores(self) -> str:
        """
        Obtener actores de la pelicula

        Return
        ------
        actores : str
            actores de la pelicula
        """
        return self.actores

    def getproductora(self) -> str:
        """
        Obtener productora de la pelicula

        Return
        ------
        productora : str
            productora de la pelicula
        """
        return self.productora

    def getpais(self) -> str:
        """
        Obtener pais de la pelicula

        Return
        ------
        pais : str
            pais de la pelicula
        """
        return self.pais

    def getfecha(self) -> str:
        """
        Obtener fecha de la pelicula

        Return
        ------
        fecha : str
            fecha de la pelicula
        """
        return self.fecha

    def setnombre(self, nombre: str):
        """
        Cambiar nombre de la pelicula

        Parametros
        ----------
        nombre : str
            nuevo nombre de la pelicula
        """
        self.nombre = nombre

    def setgenero(self, genero: str):
        """
        Cambiar genero de la pelicula

        Parametros
        ----------
        genero : str
            nuevo genero de la pelicula
        """
        self.genero = genero

    def setduracion(self, duracion: str):
        """
        Cambiar duracion de la pelicula

        Parametros
        ----------
        duracion : str
            nueva duracion de la pelicula
        """
        self.duracion = duracion

    def setclasificacion(self, clasificacion: str):
        """
        Cambiar clasificacion de la pelicula

        Parametros
        ----------
        clasificacion : str
            nueva clasificacion de la pelicula
        """
        self.clasificacion = clasificacion

    def setidioma(self, idioma: str):
        """
        Cambiar idioma de la pelicula

        Parametros
        ----------
        idioma : str
            nuevo idioma de la pelicula
        """
        self.idioma = idioma

    def setsubtitulos(self, subtitulos: str):
        """
        Cambiar subtitulos de la pelicula

        Parametros
        ----------
        subtitulos : str
            nuevos subtitulos de la pelicula
        """
        self.subtitulos = subtitulos

    def setsinopsis(self, sinopsis: str):
        """
        Cambiar sinopsis de la pelicula

        Parametros
        ----------
        sinopsis : str
            nueva sinopsis de la pelicula
        """
        self.sinopsis = sinopsis

    def setdirector(self, director: str):
        """
        Cambiar director de la pelicula

        Parametros
        ----------
        director : str
            nuevo director de la pelicula
        """
        self.director = director

    def setactores(self, actores: str):
        """
        Cambiar actores de la pelicula

        Parametros
        ----------
        actores : str
            nuevos actores de la pelicula
        """
        self.actores = actores

    def setproductora(self, productora: str):
        """
        Cambiar productora de la pelicula

        Parametros
        ----------
        productora : str
            nueva productora de la pelicula
        """
        self.productora = productora

    def setpais(self, pais: str):
        """
        Cambiar pais de la pelicula

        Parametros
        ----------
        pais : str
            nuevo pais de la pelicula
        """
        self.pais = pais

    def setfecha(self, fecha: str):
        """
        Cambiar fecha de la pelicula

        Parametros
        ----------
        fecha : str
            nueva fecha de la pelicula
        """
        self.fecha = fecha

    def getdata(self) -> dict:
        """
        Obtener datos de la pelicula

        Return
        ------
        dict
            datos de la pelicula
        """
        return {
            "nombre": self.nombre,
            "genero": self.genero,
            "duracion": self.duracion,
            "clasificacion": self.clasificacion,
            "idioma": self.idioma,
            "subtitulos": self.subtitulos,
            "sinopsis": self.sinopsis,
            "director": self.director,
            "actores": self.actores,
            "productora": self.productora,
            "pais": self.pais,
            "fecha": self.fecha,
        }

    def __str__(self) -> str:
        """
        Obtener representacion en string de la pelicula

        Return
        ------
        str
            representacion en string de la pelicula
        """
        return f"""Pelicula: \n
        id: {self.id} 
        nombre: {self.nombre}
        genero: {self.genero}
        duracion: {self.duracion}
        clasificacion: {self.clasificacion}
        idioma: {self.idioma}
        subtitulos: {self.subtitulos}
        sinopsis: {self.sinopsis}
        director: {self.director}
        actores: {self.actores}
        productora: {self.productora}
        pais: {self.pais}
        fecha: {self.fecha}
        """
