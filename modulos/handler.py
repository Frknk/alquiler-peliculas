"""

Sistema de Manejo de Archivos
YML - YAML Ain't Markup Language

@Frknk
"""

import os

from modulos import pelicula

class Handler:

    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    def crear_data_folders(self):

        """
        Crear folder de datos si no existe

        -> data
            -> peliculas
            -> usuarios
            -> encargados
        """

        if not os.path.exists('data'):
            os.makedirs('data')
            os.makedirs('data/peliculas')
            os.makedirs('data/usuarios')
            os.makedirs('data/encargados')

    
    def ingresar_pelicula(self, Pelicula):
        
        """
        Ingresar pelicula a la base de datos

        -> data
            -> peliculas x  
                -> id.txt
        """

        if not os.path.exists('data/peliculas/' + Pelicula.id + '.txt'):
            archivo = open('data/peliculas/' + Pelicula.id + '.txt', 'w')
            archivo.write(Pelicula.id + '\n')
            archivo.write(Pelicula.nombre + '\n')
            archivo.write(Pelicula.genero + '\n')
            archivo.write(Pelicula.duracion + '\n')
            archivo.write(Pelicula.clasificacion + '\n')
            archivo.write(Pelicula.idioma + '\n')
            archivo.write(Pelicula.subtitulos + '\n')
            archivo.write(Pelicula.sinopsis + '\n')
            archivo.write(Pelicula.director + '\n')
            archivo.write(Pelicula.actores + '\n')
            archivo.write(Pelicula.productora + '\n')
            archivo.write(Pelicula.pais + '\n')
            archivo.write(Pelicula.anio + '\n')
            archivo.close()
            return True
        else:
            return False
        

if __name__ == '__main__':
    handler = Handler()
    handler.crear_data_folders()
    pelicula = pelicula.Pelicula('nombre', 'genero', 'duracion', 'clasificacion', 'idioma', 'subtitulos', 'sinopsis', 'director', 'actores', 'productora', 'pais', 'anio')
    handler.ingresar_pelicula(pelicula)