def main():
    from gui.interfaz import InterfazApp
    from persistencia.gestor_archivos import GestorArchivos

    gestor = GestorArchivos('datos.txt')    
    interfaz = InterfazApp(gestor)

    interfaz.iniciar()

if __name__ == '__main__':
    main()




