# Se definen las funciones que sirven para manipular los productos

import os
import csv # CSV = Comma-Separated Values: utiliza los metodos read() y write() para manejar la base_datos.csv con separacion de comas, writerows convierte la lista productos como sublistas producto con comas y los almacena por filas.
from colorama import Fore, Style, Back, init
init(autoreset=True)
NOMBRE = 0 # producto[0]: NOMBRE, producto[1]: CATEGORIA, producto[2]: PRECIO

"""
Genera un producto a partir del nombre, categoria y precio ingresados por teclado
Ingresa el producto a la lista de productos
Parámetros:
productos(list): lista de productos
Retorna:-
""" 
def ingresar_producto ( productos ):
	print ("--- NUEVO PRODUCTO ---")
	while True:
		nombre = input(Fore.YELLOW + "Ingrese el nombre del producto: ").strip()
		if nombre != "":
			break
		print(Fore.RED + "ERROR: NOMBRE DE PRODUCTO ESTA VACIA")

	while True:
		categoria = input(Fore.YELLOW + "Ingrese la categoría del producto: ").strip()
		if categoria != "":
			break
		print(Fore.RED + "ERROR: NOMBRE DE LA CATEGORIA ESTA VACIA")

	while True:
		#Bloque para atrape el error de conversion de cadena a entero
		try:
			precio = int(input(Fore.YELLOW + "Ingrese el precio del producto (sin centavos): "))
			if precio < 0:
				print(Fore.RED + "ERROR: EL PRECIO INGRESADO ES NEGATIVO")
				continue
			break
		except ValueError:
			print(Fore.RED + "ERROR: EL PRECIO NO ES UN VALOR ENTERO")

	producto = [nombre, categoria, precio]
	
	# Insertar producto en la lista de productos ordenado por nombre
	producto_fue_insertado = False
	for indice in range(len(productos)):#i va de 0 hasta len(productos)-1
		# compara ignorando mayúsculas/minúsculas
		if nombre.lower() < productos[indice][NOMBRE].lower():  
			productos.insert (indice, producto)
			producto_fue_insertado = True
			break
	# Si no fue ingresado producto en la lista de productos,
	# debido a que al compararlo no hubo otro nombre menor alfabeticamente,
	# Simplemente de agrega el producto al final de la lista productos 
	if not producto_fue_insertado:
		productos.append(producto)

"""
Muestra por terminal la lista de productos
con el formato: nombre|categoria|precio
Parámetros:
productos(list): lista de productos
Retorna:-
""" 
def mostrar_productos ( productos ) :
    if len (productos) == 0:
        print (Fore.RED + "No hay productos registrados.")
        return

    print (Fore.BLUE +  "--- LISTA DE PRODUCTOS REGISTRADOS ---")
    # Empieza a enumerar desde 1 el i, y va deserializando producto de la lista_productos
    for indice, producto in enumerate( productos , start = 1 ):
        nombre, categoria, precio = producto
        print(Fore.YELLOW +  f"{indice}. NOMBRE: {nombre} | CATEGORÍA: {categoria} | PRECIO: ${precio}")

"""
Busca en la lista de productos los productos que coinciden con el nombre de productos
ingresado por teclado. Luegos los muestra por terminal en caso de encontrarlo
Parámetros:
productos(list): lista de productos
Retorna:-
""" 
def buscar_producto ( productos ):
	print (Fore.BLUE +  "--- BUSQUEDA DE PRODUCTO ---")
	# Borra espacios de los bordes y lo paso a minusculas
	nombre = input(Fore.GREEN + "Ingresar el nombre del producto a buscar: ").strip().lower()
	if nombre == "":
		print(Fore.RED + "ERROR: NOMBRE DE PRODUCTO A BUSCAR ESTA VACIA")
		return

	encontrados = []
	for producto in productos:
		if nombre in producto[NOMBRE].lower(): 
			encontrados.append(producto)

	if len(encontrados) != 0:
		for indice, encontrado in enumerate ( encontrados , start = 1 ) :
			nombre, categoria, precio = encontrado
			print(Fore.CYAN + f"{indice}. Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")
	else:
		print(Fore.RED + "NOMBRE DE PRODUCTO NO ESTA EN EL INVENTARIO")

"""
Elimina un producto de la lista de productos a partir de la posicion mostrada por terminal
Parámetros:
productos(list): lista de productos
Retorna:-
""" 
def eliminar_producto ( productos ):
	print ("--- ELIMINACION DE PRODUCTO ---")
	if len(productos) == 0:
		print (Fore.RED + "INVENTARIO ESTÁ VACIO")
		return

	mostrar_productos(productos)  
	while True:
		try:
			indice = int(input(Fore.GREEN + "Ingrese el número del producto a eliminar: "))
			if 1 <= indice and indice <= len(productos):
				#Se resta 1 porque la posicion en la lista empieza en 0 
				eliminado = productos.pop ( indice - 1 ) 
				break
			else:
				print(Fore.RED + "ERROR: OPCION DE LA LISTA DE PRODUCTOS FUERA DE RANGO")
		except ValueError:
			print(Fore.RED + "ERROR: INGRESO DE UN NUMERO NO ENTERO")

def cargar_productos (archivo='base_datos.csv'):
	productos = []
	if os.path.exists (archivo):
		with open (archivo, 'r', newline = '') as base_datos:	
			productos_csv = csv.reader(base_datos)
			for producto in productos_csv:
				nombre, categoria, precio = producto[0], producto[1], int(producto[2])
				productos.append ([nombre, categoria, precio])
	return productos
	
def guardar_productos (productos, archivo='base_datos.csv'):
    with open(archivo, 'w', newline='') as base_datos:
        productos_csv = csv.writer (base_datos)
        productos_csv.writerows (productos)

