import persona
import uuid
import os
import yaml

class Cliente(persona.Persona):

    def __init__(self, nombre, apellido, dni, direccion, telefono, email):
        super().__init__(nombre, apellido, dni, direccion, telefono, email)
        self.id_cliente = self.crear_id_unica()

    def generar_id(self):
        return str(uuid.uuid4().int)[:6]
    
    def crear_id_unica(self):

        """ 
        Checar si el id ya existe
        Si existe, crear otro
        Si no existe, retornar el id
        """

        # Variable que contiene la ruta del archivo
        data_file = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'data', 'usuarios_data.yml')

        if not os.path.exists(data_file): # Si no existe el archivo 
            pass

        with open(data_file, 'r') as archivo: # Abrir el archivo
            data = yaml.load(archivo, Loader=yaml.FullLoader) # Cargar el archivo
    
        try: 
            while True: # Mientras no se encuentre un id unico
                id = self.generar_id()
                if id not in data['usuarios']:
                    return id
        except TypeError:
            return self.generar_id() # Si no hay usuarios, retornar un id

if __name__ == '__main__':

    cliente1 = Cliente("Juan", "Perez", "12345678", "Av. Siempreviva 123", "123456789", "")
    
    print(cliente1)

    cliente1.setNombre("Pedro")

    print(cliente1)

        