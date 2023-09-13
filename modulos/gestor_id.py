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
    def generar_id():
        # Generar un id de 6 caracteres alfanumericos
        return str(uuid.uuid4().int)[:6]

    @classmethod
    def crear_id_unica(cls, data_file):
        """
        Checar si el id ya existe
        Si existe, crear otro
        Si no existe, retornar el id

        Parametros
        ----------
        data_file : str
            ruta del archivo de datos
            formato: "data/peliculas_data.yml"
        """

        # Verificar si data_file existe
        if not os.path.exists(data_file):
            data = {}
            print(f"El archivo {data_file} no existe")
        else:
            with open(data_file, "r") as archivo:
                data = yaml.load(archivo, Loader=yaml.FullLoader)

        # Verificar si data es un diccionario
        if not isinstance(data, dict):
            data = {}

        # Generar id unica
        try:
            while True:
                id_gen = cls.generar_id()
                if id_gen not in data:
                    return id_gen
        except Exception as e:
            print(f"A ocurrido un error al generar la id: {e}")


if __name__ == "__main__":
    asd = GestorID.crear_id_unica("test.yml")
    print(asd)
