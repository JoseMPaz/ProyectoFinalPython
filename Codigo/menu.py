#Importa el módulo estándar os, esto proporciona 
#funciones para interactuar con el sistema operativo.
import os
import opciones

from colorama import Fore, Style, Back, init
init(autoreset=True)

from metodos_productos import (
	ingresar_producto, 
	mostrar_productos,
	buscar_producto,
	eliminar_producto
)

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
    
"""
Muestra las opciones del menu por la terminal
Parámetros:-
Retorna:-
"""
def mostrar_menu():
    print(Fore.BLUE + Back.CYAN + "--- MENÚ DE OPCIONES ---" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Ingresar un nuevo producto")
    print(Fore.YELLOW + "2. Ver productos registrados")
    print(Fore.YELLOW + "3. Buscar producto por nombre")
    print(Fore.YELLOW + "4. Eliminar un producto")
    print(Fore.RED + "5. Salir")
    
"""
Muestra las opciones del menu por la terminal
Parámetros:-
Retorna:la opcion que se ingreso por teclado, 
eliminando los espacios en blanco al inicio y al final
"""    
def ingresar_opcion ():
	opcion = input ( Fore.GREEN + "Seleccionar una opción (1-5): " ).strip()
	return opcion

"""
Realiza la opcion sobre la lista de productos
Parámetros:- opcion a realizar y la lista de productos
Retorna:Bool para indicar si debe seguir pidiendo opciones o no
""" 
def ejecutar_opcion ( opcion , productos ) :
	match opcion:
		case opciones.INGRESAR_NUEVO_PRODUCTO:
			limpiar_pantalla()
			ingresar_producto(productos)
		case opciones.MOSTRAR_PRODUCTOS_POR_TERMINAL:
			limpiar_pantalla()
			mostrar_productos(productos)
		case opciones.BUSCAR_PRODUCTO_POR_NOMBRE:
			limpiar_pantalla()
			buscar_producto(productos)
		case opciones.ELIMINAR_PRODUCTO_POR_INDICE:
			limpiar_pantalla()
			eliminar_producto(productos)
		case opciones.FINALIZAR_PROGRAMA:
			return False  # salir del programa
		case _:
			print(Fore.RED + "ERROR: OPCIÓN FUERA DEL RANGO")

	input(Fore.MAGENTA + "Presione ENTER para continuar")
	return True  # continuar el bucle
    
