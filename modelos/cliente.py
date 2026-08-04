class Cliente:
    def __init__(self, dni, nombre, email, telefono, tipo_cliente):
        self.validar_dni(dni)
        self.__nombre = nombre
        self.validar_email(email)  
        self.validar_telefono(telefono)
        self.validar_tipo(tipo_cliente)

    @property
    def dni(self):
            return self.__dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def email(self):
        return self.__email

    @property
    def telefono(self):
        return self.__telefono

    @property
    def tipo(self):
        return self.__tipo_cliente

    def __str__(self):
            return (f'\nCLIENTE - \nDNI: {self.__dni} | \nNombre: {self.__nombre} | \nCorreo: {self.__email} | \nTeléfono: {self.__telefono} | \nTipo cliente : {self.__tipo_cliente}'
            )

    def __eq__(self, otro):
            if isinstance(otro, Cliente):
                return self.__dni == otro.__dni
            return False

    def validar_email(self, email):
        if '@' not in email:
            raise ValueError('Correo electrónico inválido')
        self.__email = email

    def validar_dni(self, dni):
            if not dni.isdigit():
                raise ValueError('DNI inválido')
            self.__dni = dni

    def validar_telefono(self, telefono):
        if not telefono.isdigit():
            raise ValueError("El telefono solo puede contener numeros")
        self.__telefono = telefono

    
    def validar_tipo(self, tipo_cliente):
        tipo_cliente = tipo_cliente.strip().lower()
        if tipo_cliente not in ['regular', 'premium', 'corporativo']:
            raise ValueError("El tipo de cliente ingresado no es válido")
        self.__tipo_cliente = tipo_cliente

    def to_linea_txt(self):
        return f'{self.__dni},{self.__nombre},{self.__email},{self.__telefono},{self.__tipo_cliente}'
    
        
    
            