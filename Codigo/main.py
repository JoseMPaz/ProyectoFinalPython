# Pre_Entrega
# Alumno: Paz Portilla, Jose Miguel
# Comision: 25010

#De metodos_productos.py importa los metodos: 
#ingresar_producto, mostrar_productos, buscar_producto, eliminar_producto.
from metodos_productos import ( 
	ingresar_producto,
	mostrar_productos,
	buscar_producto,
	eliminar_producto,
	cargar_productos,
	guardar_productos
)

#De menu.py importa los metodos: 
#limpiar_pantalla, mostrar_menu, ejecutar_opcion, ingresar_opcion.
from menu import (
	limpiar_pantalla,
	mostrar_menu,
	ejecutar_opcion,
	ingresar_opcion 
)
    
"""
Es el programa principal, repetitivamente limpia la terminal(hasta ingresar terminar program), 
muestra un menu de opciones, toma la opcion y realiza alguna accion sobre productos a partir de ella.
Parámetros:-
Retorna:-
""" 
def main () :
	
	productos = cargar_productos()
	volver_al_menu = True
	
	while volver_al_menu == True : 
		limpiar_pantalla () 
		mostrar_menu () 
		opcion = ingresar_opcion ()
		volver_al_menu = ejecutar_opcion ( opcion , productos ) 
	guardar_productos(productos)
	limpiar_pantalla ()
	print("\n\n\t\t¡PROGRAMA FINALIZADO!\n\n")
		

if __name__ == "__main__":
    main()
    
