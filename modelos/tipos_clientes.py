from modelos.cliente import Cliente


class ClienteRegular(Cliente):
    def __init__(self, dni, nombre, email, telefono):
        super().__init__(dni, nombre, email, telefono, 'Regular')

class ClientePremium(Cliente):
    def __init__(self, dni, nombre, email, telefono):
            super().__init__(dni, nombre, email, telefono, 'Premium')

class ClienteCorporativo(Cliente):
    def __init__(self, dni, nombre, email, telefono ):
            super().__init__(dni, nombre, email, telefono, 'Corporativo')
    
    

    

    