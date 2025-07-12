from colorama import Fore, Style, init
import productos
import os

init(autoreset=True)

"""
Refresca o limpia la terminal
Parámetros:-
Retorna:-
"""
def limpiar_pantalla():
	# os.system: Ejecuta un comando del sistema operativo 
	# como si se escribiera en la terminal.
	# Si el nombre del sistema operativo es windows utiliza cls,
	# sino utiliza clear para refrescar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print(Fore.CYAN + "\n--- MENÚ DE OPCIONES ---")
    print(Fore.YELLOW + "1." + Fore.RESET + " Registrar nuevo producto")
    print(Fore.YELLOW + "2." + Fore.RESET + " Ver productos")
    print(Fore.YELLOW + "3." + Fore.RESET + " Actualizar producto")
    print(Fore.YELLOW + "4." + Fore.RESET + " Eliminar producto")
    print(Fore.YELLOW + "5." + Fore.RESET + " Buscar producto por ID")
    print(Fore.YELLOW + "6." + Fore.RESET + " Buscar por nombre o categoría")
    print(Fore.YELLOW + "7." + Fore.RESET + " Reporte de stock bajo")
    print(Fore.YELLOW + "8." + Fore.RESET + " Salir")

def ejecutar_opcion(opcion):
    match opcion:
        case "1":
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            categoria = input("Categoría: ")
            productos.agregar(nombre, descripcion, cantidad, precio, categoria)
            print(Fore.GREEN + "Producto registrado.")

        case "2":
            for producto in productos.listar():
                print(producto)

        case "3":
            pid = int(input("ID del producto a actualizar: "))
            p = productos.buscar_por_id(pid)
            if p:
                nombre = input(f"Nuevo nombre ({p[1]}): ") or p[1]
                descripcion = input(f"Nueva descripción ({p[2]}): ") or p[2]
                cantidad = int(input(f"Nueva cantidad ({p[3]}): ") or p[3])
                precio = float(input(f"Nuevo precio ({p[4]}): ") or p[4])
                categoria = input(f"Nueva categoría ({p[5]}): ") or p[5]
                productos.actualizar(pid, nombre, descripcion, cantidad, precio, categoria)
                print(Fore.GREEN + "Producto actualizado.")
            else:
                print(Fore.RED + "Producto no encontrado.")

        case "4":
            pid = int(input("ID del producto a eliminar: "))
            productos.eliminar(pid)
            print(Fore.RED + "Producto eliminado.")

        case "5":
            pid = int(input("ID del producto: "))
            p = productos.buscar_por_id(pid)
            print(p if p else Fore.RED + "Producto no encontrado.")

        case "6":
            tipo = input("Buscar por (n)ombre o (c)ategoría: ").lower()
            if tipo == "n":
                nombre = input("Nombre: ")
                encontrados = productos.buscar_por_nombre(nombre)
            elif tipo == "c":
                categoria = input("Categoría: ")
                encontrados = productos.buscar_por_categoria(categoria)
            else:
                print(Fore.RED + "Opción inválida.")
                return
            for p in encontrados:
                print(p)

        case "7":
            limite = int(input("Mostrar productos con stock <=: "))
            for p in productos.stock_bajo(limite):
                print(p)

        case "8":
            print(Fore.CYAN + "¡Programa Finalizado!")
            exit()

        case _:
            print(Fore.RED + "Opción inválida.")
