"""
@Frknk

Clases:
    - Cliente

Atributos:
    None

Funciones:
    - Cliente() : Constructor de la clase Cliente.
"""

from modulos.persona import Persona
from modulos.gestor_id import GestorID


class Cliente(Persona):
    """
    Clase para manejar los clientes

    ...

    Atributos
    ---------
    id : str
        id del cliente
    password : str
        password del cliente


    """

    def __init__(
        self,
        nombre: str,
        apellido: str,
        dni: str,
        direccion: str,
        telefono: str,
        email: str,
        password: str,
    ):
        """
        Constructor de la clase Cliente

        Parametros
        ----------
        nombre : str
            nombre del cliente
        apellido : str
            apellido del cliente
        dni : str
            dni del cliente
        direccion : str
            direccion del cliente
        telefono : str
            telefono del cliente
        email : str
            email del cliente
        password : str
            password del cliente
        """
        super().__init__(nombre, apellido, dni, direccion, telefono, email)
        self.id = GestorID.crear_id_unica("data/clientes_data.yml")
        self.password = password

    def getid(self) -> str:
        """
        Obtener el id del cliente

        Return
        ------
        str
            id del cliente
        """
        return self.id

    def getpassword(self) -> str:
        """
        Obtener el password del cliente

        Return
        ------
        str
            password del cliente
        """
        return self.password

    def setpassword(self, password: str) -> None:
        """
        Asignar un password al cliente

        Parametros
        ----------
        password : str
            password del cliente
        """
        self.password = password
