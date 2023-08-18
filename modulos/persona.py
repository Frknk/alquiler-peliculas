class Persona:

    def __init__(self, nombre, apellido, dni, direccion, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def getDatosString(self):
        return f"{self.nombre} {self.apellido} {self.dni} {self.direccion} {self.telefono} {self.email}"
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setDni(self, dni):
        self.dni = dni

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setEmail(self, email):
        self.email = email

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getDni(self):
        return self.dni
    
    def getDireccion(self):
        return self.direccion
    
    def getTelefono(self):
        return self.telefono
    
    def getEmail(self):
        return self.email
    
    # Por si lo llamo en un str o print
    def __str__(self):
        return self.getDatosString()

if __name__ == '__main__':
    datos_persona = {
    "nombre": "Juan",
    "apellido": "Perez",
    "dni": "12345678",
    "direccion": "Av. Siempreviva 123",
    "telefono": "123456789",
    "email": "asd@gmail.com"
    }
    persona = Persona(**datos_persona)
    print(persona.getDatosString())
    print(persona)