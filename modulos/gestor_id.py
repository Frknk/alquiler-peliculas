"""
@Frknk

Clases:
    - GestorID

Atributos:
    - None

Funciones:
    - GestorID() : Constructor de la clase GestorID.
"""
import os
import uuid

import yaml


class GestorID:
    """
    Clase para manejar los identificadores unicos

    ...

    Atributos
    ---------
    None

    Metodos
    -------
    generar_id()
        Genera un identificador unico de 6 caracteres alfanumericos usando uuid4.
    crear_id_unica()
        Comprueba la existencia de un id en un archivo de datos. Si ya existe, genera otro id.
        Si no retorna el id generado.
    """

    @staticmethod
    def generar_id() -> str:
        # Generar un id de 6 caracteres alfanumericos
        # Preferible si no buscas crear un id unico
        return str(uuid.uuid4().int)[:6]

    @classmethod
    def crear_id_unica(cls, data_file) -> str:
        """
        Checar si el id ya existe en un archivo de datos
        Si existe, crear otro
        Si no existe, retornar el id

        Parametros
        ----------
        data_file : str
            ruta del archivo de datos
            ejemplo: "data/peliculas_data.yml"

        Return
        ------
        id_gen : str
            id generado
        """

        # Verificar si data_file existe
        if not os.path.exists(os.getcwd() + "/" + data_file):  # Obtener directorio actual
            print(f"El archivo {data_file} no existe en {os.getcwd()}")
            return "NULL ID"
        else:
            with open(data_file, "r") as archivo:
                data = yaml.load(archivo, Loader=yaml.FullLoader)

        # Verificar si data es un diccionario
        if not isinstance(data, dict):
            data = {}

        # Loop para generar id unica
        try:
            while True:
                # Generar id
                id_gen = cls.generar_id()
                # Verificar si id_gen ya existe en data
                if id_gen not in data:
                    return id_gen
        except Exception as e:
            print(f"A ocurrido un error al generar la id: {e}")
