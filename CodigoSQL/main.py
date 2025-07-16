from productos import crear_base
from menu import mostrar_menu, ejecutar_opcion, limpiar_pantalla
from colorama import Fore, Style, init

def main():
    crear_base()
    while True:
        limpiar_pantalla ()
        mostrar_menu ()
        opcion = input (Fore.BLUE +"Selecciona una opción: ")
        limpiar_pantalla ()
        ejecutar_opcion (opcion)
        input (Fore.MAGENTA + "Presione ENTER para continuar")

if __name__ == "__main__":
    main()
