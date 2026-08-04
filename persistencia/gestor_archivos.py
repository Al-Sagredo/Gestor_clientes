from modelos.cliente import Cliente
from modelos.tipos_clientes import ClienteRegular, ClientePremium, ClienteCorporativo

class GestorArchivos:
    def __init__(self, nombre_archivo):
        self.__nombre_archivo = nombre_archivo
        self.__clientes = self.cargar_clientes()

    def cargar_clientes(self):
            '''
            abre el archivo, extrae los datos de los clientes, crea un objeto cliente para cada uno y los 
            guarda en una lista de clientes.
            '''
            clientes = []
            try:
                #abre el archivo en modo lectura
                with open(self.__nombre_archivo, 'r') as archivo:
                    linea = archivo.readline()
                    #lee linea por linea hasta que ya no hay nada mas para leer
                    while linea != '':
                        #transforma cada linea en una lista
                        datos_cliente = linea.strip().split(',')
                        #desempaquetado de la lista
                        dni, nombre, email, telefono, tipo_cliente = datos_cliente
                        #clasifica al cliente y crea el objeto correspondiente
                        if tipo_cliente == 'regular':
                            cliente = ClienteRegular(dni, nombre, email, telefono)
                        elif tipo_cliente == 'premium':
                            cliente = ClientePremium(dni, nombre, email, telefono)
                        elif tipo_cliente == 'corporativo':
                            cliente = ClienteCorporativo(dni, nombre, email, telefono)
                        else:
                            cliente = Cliente(dni,nombre, email, telefono, tipo_cliente)
                        #agrega el cliente a la lista
                        clientes.append(cliente)
                        linea = archivo.readline()
                return clientes
    
            except FileNotFoundError:
                return []

    def agregar_cliente(self, cliente):
        busqueda = self.buscar_cliente(cliente.dni)
        if busqueda:
            return 'El DNI ya se encuentra registrado'
        else:
            self.__clientes.append(cliente)
            self.guardar_clientes(self.__clientes)
            return True

    def buscar_cliente(self, dni):
            for cliente in self.__clientes:
                if cliente.dni == dni:
                    return cliente
            return None

    def guardar_clientes(self, lista_clientes):
            with open(self.__nombre_archivo, 'w') as archivo:
                for cliente in lista_clientes:
                    archivo.write(cliente.to_linea_txt() + '\n')

    def obtener_clientes(self):
            return self.__clientes

    def eliminar_cliente(self, dni):
            busqueda = self.buscar_cliente(dni)
            if busqueda:
                self.__clientes.remove(busqueda)
                self.guardar_clientes(self.__clientes)
                return True
            else:
                return False

    def editar_cliente(self,dni):
         pass



            
            

    
