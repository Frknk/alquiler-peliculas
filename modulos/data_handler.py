"""
Sistema de Manejo de Archivos
YML - YAML Ain't Markup Language

@Frknk
"""

import os
import yaml
import pelicula


class Handler:
    """
    Constructor de la clase Handler
    """

    def __init__(self):
        self.root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Obtener directorio raiz

    def crear_data(self):

        """
        Crear folder data
        Crear peliculas_data.yml, usuarios_data.yml y encargados_data.yml

        -> data (0)
            - peliculas_data.yml (0)
            - usuarios_data.yml (0)
            - encargados_data.yml (0)
        """

        # Si el folder data no existe, crearlo
        if not os.path.exists(os.path.join(self.root_dir, 'data')):
            os.mkdir(os.path.join(self.root_dir, 'data'))

        # Si el archivo peliculas_data.yml no existe, crearlo
        if not os.path.exists(os.path.join(self.root_dir, 'data', 'peliculas_data.yml')):
            with open(os.path.join(self.root_dir, 'data', 'peliculas_data.yml'), 'w') as archivo:
                archivo.write('peliculas:')

        # Si el archivo usuarios_data.yml no existe, crearlo
        if not os.path.exists(os.path.join(self.root_dir, 'data', 'usuarios_data.yml')):
            with open(os.path.join(self.root_dir, 'data', 'usuarios_data.yml'), 'w') as archivo:
                archivo.write('usuarios:')

        # Si el archivo encargados_data.yml no existe, crearlo
        if not os.path.exists(os.path.join(self.root_dir, 'data', 'encargados_data.yml')):
            with open(os.path.join(self.root_dir, 'data', 'encargados_data.yml'), 'w') as archivo:
                archivo.write('encargados:')

    def ingresar_pelicula(self, Pelicula):

        """
        Ingresar pelicula al archivo peliculas_data.yml

        -> data
            -> peliculas_data.yml
                -> pelicula_id (0)
                    - nombre
                    - genero
                    - duracion
                    - clasificacion
                    - idioma
                    - subtitulos
                    - sinopsis
                    - director
                    - actores
                    - productora
                    - pais
                    - anio
        """

        # Crear pelicula_id
        pelicula_id = Pelicula.id

        # Crear diccionario de pelicula
        pelicula_dict = {
            pelicula_id: {
                'nombre': Pelicula.nombre,
                'genero': Pelicula.genero,
                'duracion': Pelicula.duracion,
                'clasificacion': Pelicula.clasificacion,
                'idioma': Pelicula.idioma,
                'subtitulos': Pelicula.subtitulos,
                'sinopsis': Pelicula.sinopsis,
                'director': Pelicula.director,
                'actores': Pelicula.actores,
                'productora': Pelicula.productora,
                'pais': Pelicula.pais,
                'anio': Pelicula.anio
            }
        }

        # Abrir peliculas_data.yml
        with open(os.path.join(self.root_dir, 'data', 'peliculas_data.yml'), 'r') as archivo:
            # Cargar peliculas_data.yml
            peliculas_data = yaml.safe_load(archivo)
            if peliculas_data['peliculas'] is None:
                peliculas_data['peliculas'] = {}

        # Agregar pelicula_dict a peliculas_data
        peliculas_data['peliculas'].update(pelicula_dict)

        # Abrir peliculas_data.yml
        with open(os.path.join(self.root_dir, 'data', 'peliculas_data.yml'), 'w') as archivo:
            # Guardar peliculas_data.yml
            yaml.dump(peliculas_data, archivo)

    def eliminar_pelicula(self, pelicula_id):

        """
        Eliminar pelicula del archivo peliculas_data.yml
        :param pelicula_id: id de la pelicula a eliminar

        -> data
            -> peliculas_data.yml
                -> pelicula_id (X)
                    - nombre
                    - genero
                    - duracion
                    - clasificacion
                    - idioma
                    - subtitulos
                    - sinopsis
                    - director
                    - actores
                    - productora
                    - pais
                    - anio
        """

        # Abrir peliculas_data.yml
        with open(os.path.join(self.root_dir, 'data', 'peliculas_data.yml'), 'r') as archivo:
            # Cargar peliculas_data.yml
            peliculas_data = yaml.safe_load(archivo)

        # Verificar si pelicula_id existe en peliculas_data
        if pelicula_id not in peliculas_data['peliculas']:
            return

        # Eliminar pelicula_id de peliculas_data
        peliculas_data['peliculas'].pop(pelicula_id)

        # Abrir peliculas_data.yml
        with open(os.path.join(self.root_dir, 'data', 'peliculas_data.yml'), 'w') as archivo:
            # Guardar peliculas_data.yml
            yaml.dump(peliculas_data, archivo)

    def modificar_pelicula(self, pelicula_id, campo, nuevo_valor):

        """
        Modificar pelicula del archivo peliculas_data.yml
        :param pelicula_id: id de la pelicula a modificar
        :param campo: campo a modificar
        :param nuevo_valor: nuevo valor del campo

        -> data
            -> peliculas_data.yml
                -> pelicula_id  (-)
                    - nombre
                    - genero
                    - duracion
                    - clasificacion
                    - idioma
                    - subtitulos
                    - sinopsis
                    - director
                    - actores
                    - productora
                    - pais
                    - anio

        """

        # Buscar pelicula_id en peliculas_data.yml
        with open(os.path.join(self.root_dir, 'data', 'peliculas_data.yml'), 'r') as archivo:
            peliculas_data = yaml.safe_load(archivo)

        # Verificar si pelicula_id existe en peliculas_data
        if pelicula_id not in peliculas_data['peliculas']:
            return

        # Cargar datos de pelicula_id en un diccionario
        pelicula_dict = peliculas_data['peliculas'][pelicula_id]

        # Modificar campo de pelicula_dict
        pelicula_dict[campo] = nuevo_valor

        # Actualizar pelicula_id en peliculas_data
        peliculas_data['peliculas'][pelicula_id] = pelicula_dict

        # Abrir peliculas_data.yml
        with open(os.path.join(self.root_dir, 'data', 'peliculas_data.yml'), 'w') as archivo:
            # Guardar peliculas_data.yml
            yaml.dump(peliculas_data, archivo)


if __name__ == '__main__':
    handler = Handler()
    handler.crear_data()
    pelicula = pelicula.Pelicula('nombre', 'genero', 'duracion', 'clasificacion', 'idioma', 'subtitulos', 'sinopsis',
                                 'director', 'actores', 'productora', 'pais', 'fecha')
    handler.ingresar_pelicula(pelicula)
    handler.modificar_pelicula('303191', 'nombre', 'nuevo_nombre')
