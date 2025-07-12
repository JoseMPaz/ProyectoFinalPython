from productos import crear_base
from menu import mostrar_menu, ejecutar_opcion, limpiar_pantalla

def main():
    crear_base()
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        limpiar_pantalla()
        ejecutar_opcion(opcion)
        input("Presione ENTER para continuar")

if __name__ == "__main__":
    main()
