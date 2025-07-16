import sqlite3

def crear_base ():
    conexion = sqlite3.connect ("inventario.db")
    cursor = conexion.cursor ()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    """)
    conexion.commit ()
    conexion.close ()

def agregar (nombre, descripcion, cantidad, precio, categoria):
    conexion = sqlite3.connect ("inventario.db")
    cursor = conexion.cursor ()
    cursor.execute ("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
              (nombre, descripcion, cantidad, precio, categoria))
    conexion.commit ()
    conexion.close ()

def listar ():
    conexion = sqlite3.connect ("inventario.db")
    cursor = conexion.cursor ()
    cursor.execute ("SELECT * FROM productos")
    productos = cursor.fetchall ()
    conexion.close ()
    return productos

def buscar_por_id (identificador):
    conexion = sqlite3.connect ("inventario.db")
    cursor = conexion.cursor ()
    cursor.execute("SELECT * FROM productos WHERE id=?", (identificador,))
    producto = cursor.fetchone ()
    conexion.close ()
    return producto

def actualizar (identificador, nombre, descripcion, cantidad, precio, categoria):
    conexion = sqlite3.connect ("inventario.db")
    cursor = conexion.cursor ()
    cursor.execute ("""UPDATE productos SET nombre=?, descripcion=?, cantidad=?, precio=?, categoria=? WHERE id=?""",
              (nombre, descripcion, cantidad, precio, categoria, identificador))
    conexion.commit ()
    conexion.close ()

def eliminar (identificador):
    conexion = sqlite3.connect ("inventario.db")
    cursor = conexion.cursor ()
    cursor.execute ("DELETE FROM productos WHERE id=?", (identificador,))
    conexion.commit ()
    conexion.close ()

def buscar_por_nombre (nombre):
    conexion = sqlite3.connect ("inventario.db")
    cursor = conexion.cursor ()
    cursor.execute ("SELECT * FROM productos WHERE nombre LIKE ?", ('%' + nombre + '%',))
    productos = cursor.fetchall ()
    conexion.close ()
    return productos

def buscar_por_categoria (categoria):
    conexion = sqlite3.connect ("inventario.db")
    cursor = conexion.cursor ()
    cursor.execute ("SELECT * FROM productos WHERE categoria LIKE ?", ('%' + categoria + '%',))
    productos = cursor.fetchall ()
    conexion.close ()
    return productos

def stock_bajo (cantidad_maxima):
    conexion = sqlite3.connect ("inventario.db")
    cursor = conexion.cursor ()
    cursor.execute ("SELECT * FROM productos WHERE cantidad <= ?", (cantidad_maxima,))
    productos = cursor.fetchall ()
    conexion.close ()
    return productos
    
