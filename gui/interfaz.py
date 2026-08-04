import tkinter as tk
from tkinter import messagebox
from modelos.cliente import Cliente

class InterfazApp:
    def __init__(self, gestor):
        self.__gestor = gestor
        
        #configuracion ventana de tkinter
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de clientes")
        self.ventana.config(width=600,height=600)

        #-------ETIQUETAS Y ENTRADAS--------

        #etiqueta y entrada de DNI
        tk.Label(text='DNI').place(x=10,y=10)
        self.entry_dni = tk.Entry()
        self.entry_dni.place(x=10,y=40)

        #etiqueta y entrada del nombre del cliente
        tk.Label(text='Nombre').place(x=10,y=80)
        self.entry_nombre = tk.Entry()
        self.entry_nombre.place(x=10, y=110)

        #etiqueta y entrada email
        tk.Label(text='Email').place(x=10, y=150)
        self.entry_email = tk.Entry()
        self.entry_email.place(x=10,y=180)

        #etiqueta y entrada telefono
        tk.Label(text='Telefono').place(x=10, y=220)
        self.entry_telefono = tk.Entry()
        self.entry_telefono.place(x=10,y=250)

        #etiqueta y entrada de tipo cliente
        tk.Label(text='Tipo de cliente').place(x=10,y=290)
        self.entry_tipo = tk.Entry()
        self.entry_tipo.place(x=10,y=320)



        #--------BOTONES----------

        # Botón agregar cliente
        self.boton_agregar = tk.Button(text='Crear', command= self.agregar_cliente)
        self.boton_agregar.place(x=20, y=360, width=100, height=30)

        # Botón Buscar cliente
        self.boton_editar = tk.Button(text='Buscar', command= self.buscar_cliente)
        self.boton_editar.place(x=130, y=360, width=100, height=30)

        # Botón Eliminar cliente
        self.boton_eliminar = tk.Button(text='Eliminar', command= self.eliminar_cliente)
        self.boton_eliminar.place(x=240, y=360, width=100, height=30)

        # Botón Limpiar
        self.boton_limpiar = tk.Button(text='Limpiar', command= self.limpiar)
        self.boton_limpiar.place(x=350, y=360, width=100, height=30)


        # LISTBOX
        self.lista_clientes = tk.Listbox(width=90, height=10)
        self.lista_clientes.place(x=20,y=410)

    #-------------------METODOS---------------------
            
    def iniciar(self):
        self.mostrar_clientes()
        self.ventana.mainloop()

    def agregar_cliente(self):
        dni = self.entry_dni.get()
        nombre = self.entry_nombre.get()
        email = self.entry_email.get()
        telefono = self.entry_telefono.get()
        tipo_cliente = self.entry_tipo.get()

        #valida que todos los campos estén completados
        if not (dni.strip() and nombre.strip() and email.strip() and telefono.strip() and tipo_cliente.strip()):
            messagebox.showerror('Error', 'Rellena todos los campos')

        else:
            #crea el objeto cliente.
            try:
                cliente = Cliente(dni, nombre, email, telefono, tipo_cliente)
                #llama al metodo  para agregar el cliente
                resultado_agregar_cliente = self.__gestor.agregar_cliente(cliente)
    
                #si el metodo retorna string, es el mensaje de error de que el cliente ya existe
                if isinstance(resultado_agregar_cliente, str):
                    messagebox.showerror('Error', resultado_agregar_cliente)
                else: #si no es un string, es True: el cliente fue agregado
                    messagebox.showinfo('Correcto', 'Cliente agregado')
                    self.limpiar()
                    self.mostrar_clientes() 
                            
            except ValueError as e:
                messagebox.showerror('Error de validación', str(e)) 
                
    def buscar_cliente(self):
        dni = self.entry_dni.get()
        cliente = self.__gestor.buscar_cliente(dni)
        if cliente:
            self.cargar_formulario(cliente)
        else:
            messagebox.showerror('Error', 'Cliente no encontrado')

    def cargar_formulario(self, cliente):
        self.entry_nombre.delete(0,'end')
        self.entry_nombre.insert(0, cliente.nombre)

        self.entry_dni.delete(0,'end')
        self.entry_dni.insert(0, cliente.dni)

        self.entry_telefono.delete(0,'end')
        self.entry_telefono.insert(0, cliente.telefono)

        self.entry_email.delete(0,'end')
        self.entry_email.insert(0, cliente.email)

        self.entry_tipo.delete(0,'end')
        self.entry_tipo.insert(0, cliente.tipo)
        
    def editar_cliente(self):
        dni = self.entry_dni.get()
        nombre = self.entry_nombre.get()
        email = self.entry_email.get()
        telefono = self.entry_telefono.get()
        tipo_cliente = self.entry_tipo.get()

        #valida que todos los campos estén completados
        if not (dni.strip() and nombre.strip() and email.strip() and telefono.strip() and tipo_cliente.strip()):
            messagebox.showerror('Error', 'Rellena todos los campos')

        else:
            #crea el objeto cliente
            try:
                cliente = Cliente(dni, nombre, email, telefono, tipo_cliente)

                #llama al metodo  para agregar el cliente
                resultado_editar = self.__gestor.editar_cliente(cliente)
                if resultado_editar:
                    messagebox.showinfo('Correcto', 'Cliente actualizado')
                    self.limpiar()
                    self.mostrar_clientes() 
                else:
                    messagebox.showerror('Error', 'El DNI ingresado no existe')
            except ValueError as e:
                messagebox.showerror('Error de validación', str(e))
                




    def eliminar_cliente(self):
        dni = self.entry_dni.get()
        if not dni:
            messagebox.showerror('Error', 'EL campo DNI no puede estar vacío')
        else:
            resultado_eliminacion = self.__gestor.eliminar_cliente(dni)
            if resultado_eliminacion:
                messagebox.showinfo('Correcto', 'Cliente eliminado')
                self.limpiar()
                self.mostrar_clientes()
            else:
                messagebox.showerror('Error', 'El DNI ingresado no pertenece a ningun cliente')

        
    def mostrar_clientes(self):
        '''Limpia el listbox y lo llena con todos los clientes de la lista'''
        self.lista_clientes.delete(0,tk.END)

        lista_clientes = self.__gestor.obtener_clientes()

        for cliente in lista_clientes:
            self.lista_clientes.insert(tk.END, cliente)


    def limpiar(self):
        self.entry_dni.delete(0,tk.END)
        self.entry_nombre.delete(0,tk.END)
        self.entry_email.delete(0,tk.END)
        self.entry_telefono.delete(0,tk.END)
        self.entry_tipo.delete(0,tk.END)



