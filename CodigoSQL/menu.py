from colorama import Fore, Style, init
import productos
import os

init (autoreset=True)


"""
Refresca o limpia la terminal
Parámetros:-
Retorna:-
"""
def limpiar_pantalla ():
	# os.system: Ejecuta un comando del sistema operativo 
	# como si se escribiera en la terminal.
	# Si el nombre del sistema operativo es windows utiliza cls,
	# sino utiliza clear para refrescar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu ():
    print(Fore.CYAN + "--- MENÚ DE OPCIONES ---")
    print(Fore.YELLOW + "1.-" + Fore.RESET + " Registrar nuevo producto")
    print(Fore.YELLOW + "2.-" + Fore.RESET + " Ver productos")
    print(Fore.YELLOW + "3.-" + Fore.RESET + " Actualizar producto")
    print(Fore.YELLOW + "4.-" + Fore.RESET + " Eliminar producto")
    print(Fore.YELLOW + "5.-" + Fore.RESET + " Buscar producto por ID")
    print(Fore.YELLOW + "6.-" + Fore.RESET + " Buscar por nombre o categoría")
    print(Fore.YELLOW + "7.-" + Fore.RESET + " Reporte de stock bajo")
    print(Fore.YELLOW + "8.-" + Fore.RESET + " Salir")

def ejecutar_opcion(opcion):
    match opcion:
        case "1":
            print(Fore.BLUE +"##########################")
            print (Fore.BLUE + "### Nuevo Producto ###")
            print(Fore.BLUE + "##########################")
            nombre = input("Nombre: ")
            while nombre == "":
            	print (Fore.RED +"El nombre no puede estar vacío")
            	nombre = input("Nombre: ")   	
            descripcion = input("Descripción: ")
            cantidad = input("Cantidad: ")
            while cantidad == "":
            	print (Fore.RED +"La cantidad no puede estar vacía")
            	cantidad = input("Cantidad: ")
            try:
            	cantidad = int(cantidad)
            except ValueError:
            	print (Fore.RED +"La cantidad debe ser un valor entero")
            if cantidad <= 0:
            	print(Fore.RED +"La cantidad debe ser mayor a cero")
            	return
            precio = input("Precio: ")
            while precio == "":
            	print (Fore.RED +"El precio no puede esta vacío")
            	precio = input("Precio: ")
            try:
            	precio = float (precio)
            except ValueError:
            	print (Fore.RED +"El precio debe ser un valor real")  
            if precio <= 0.0:
            	print (Fore.RED +"El precio debe ser mayor a cero")
            	return                      
            categoria = input("Categoría: ")
            productos.agregar (nombre, descripcion, cantidad, precio, categoria)
            print(Fore.GREEN + "Producto registrado.")

        case "2":
            print(Fore.BLUE + "##########################")
            print (Fore.BLUE +"### Lista de Productos ###")
            print(Fore.BLUE + "##########################")
            for producto in productos.listar():
                print(f"Id: {producto[0]}")
                print(f"Nombre: {producto[1]}")
                print(f"Descripción: {producto[2]}")
                print(f"Cantidad: {producto[3]} [u]")
                print(f"Precio: ${producto[4]}")
                print(f"Categoría: {producto[5]}")
                print(Fore.BLUE +"##########################")
        
        case "3":
            print(Fore.BLUE + "##########################")
            print (Fore.BLUE + "### Actualizar Producto ###")
            print(Fore.BLUE + "##########################")
            identificador = int(input("ID del producto a actualizar: "))
            producto = productos.buscar_por_id (identificador)
            if producto:
                nombre = input(f"Nuevo nombre ({producto[1]}): ") or producto[1]
                descripcion = input(f"Nueva descripción ({producto[2]}): ") or producto[2]
                cantidad = int(input(f"Nueva cantidad ({producto[3]}): ") or producto[3])
                precio = float(input(f"Nuevo precio ({producto[4]}): ") or producto[4])
                categoria = input(f"Nueva categoría ({producto[5]}): ") or producto[5]
                productos.actualizar(identificador, nombre, descripcion, cantidad, precio, categoria)
                print(Fore.GREEN + "Producto actualizado.")
            else:
                print(Fore.RED + "Producto no encontrado.")

        case "4":
            print(Fore.BLUE + "##########################")
            print (Fore.BLUE + "### ELiminar Producto ###")
            print(Fore.BLUE + "##########################")
            identificador = int(input("ID del producto a eliminar: "))
            productos.eliminar (identificador)
            print(Fore.RED + "Producto eliminado.")

        case "5":
            print(Fore.BLUE + "##########################")
            print (Fore.BLUE + "### Buscar Producto por ID ###")
            print(Fore.BLUE + "##########################")
            pid = int(input("ID del producto: "))
            producto = productos.buscar_por_id(pid)
            if producto:
            	print ("Producto encontrado")
            	print(f"Id: {producto[0]}")
            	print(f"Nombre: {producto[1]}")
            	print(f"Descripción: {producto[2]}")
            	print(f"Cantidad: {producto[3]} [u]")
            	print(f"Precio: ${producto[4]}")
            	print(f"Categoría: {producto[5]}")
            else:
            	print (Fore.RED + "Producto no encontrado.")

        case "6":
            print(Fore.BLUE + "##########################")
            print (Fore.BLUE + "### Buscar Producto por Nombre o Categoría ###")
            print(Fore.BLUE + "##########################")
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
            
            if encontrados:
            	for producto in encontrados:
            		print ("Producto encontrado")
            		print(f"Id: {producto[0]}")
            		print(f"Nombre: {producto[1]}")
            		print(f"Descripción: {producto[2]}")
            		print(f"Cantidad: {producto[3]} [u]")
            		print(f"Precio: ${producto[4]}")
            		print(f"Categoría: {producto[5]}")
            else:
            	print (Fore.RED + "Producto no encontrado.")

        case "7":
            print(Fore.BLUE + "##########################")
            print (Fore.BLUE + "### Productos con poco stock ###")
            print(Fore.BLUE + "##########################")
            cantidad_maxima = int(input("Mostrar productos con stock menor o igual: "))
            for producto in productos.stock_bajo (cantidad_maxima):
                print(f"Id: {producto[0]}")
                print(f"Nombre: {producto[1]}")
                print(f"Descripción: {producto[2]}")
                print(f"Cantidad: {producto[3]} [u]")
                print(f"Precio: ${producto[4]}")
                print(f"Categoría: {producto[5]}")
                print("##########################")

        case "8":
            print(Fore.CYAN + "\n\t¡Programa Finalizado!\n")
            exit()

        case _:
            print(Fore.RED + "Opción inválida.")
