import sqlite3

def crear_base():
    conn = sqlite3.connect("inventario.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    """)
    conn.commit()
    conn.close()

def agregar(nombre, descripcion, cantidad, precio, categoria):
    conn = sqlite3.connect("inventario.db")
    c = conn.cursor()
    c.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
              (nombre, descripcion, cantidad, precio, categoria))
    conn.commit()
    conn.close()

def listar():
    conn = sqlite3.connect("inventario.db")
    c = conn.cursor()
    c.execute("SELECT * FROM productos")
    datos = c.fetchall()
    conn.close()
    return datos

def buscar_por_id(pid):
    conn = sqlite3.connect("inventario.db")
    c = conn.cursor()
    c.execute("SELECT * FROM productos WHERE id=?", (pid,))
    dato = c.fetchone()
    conn.close()
    return dato

def actualizar(pid, nombre, descripcion, cantidad, precio, categoria):
    conn = sqlite3.connect("inventario.db")
    c = conn.cursor()
    c.execute("""UPDATE productos SET nombre=?, descripcion=?, cantidad=?, precio=?, categoria=? WHERE id=?""",
              (nombre, descripcion, cantidad, precio, categoria, pid))
    conn.commit()
    conn.close()

def eliminar(pid):
    conn = sqlite3.connect("inventario.db")
    c = conn.cursor()
    c.execute("DELETE FROM productos WHERE id=?", (pid,))
    conn.commit()
    conn.close()

def buscar_por_nombre(nombre):
    conn = sqlite3.connect("inventario.db")
    c = conn.cursor()
    c.execute("SELECT * FROM productos WHERE nombre LIKE ?", ('%' + nombre + '%',))
    datos = c.fetchall()
    conn.close()
    return datos

def buscar_por_categoria(cat):
    conn = sqlite3.connect("inventario.db")
    c = conn.cursor()
    c.execute("SELECT * FROM productos WHERE categoria LIKE ?", ('%' + cat + '%',))
    datos = c.fetchall()
    conn.close()
    return datos

def stock_bajo(limite):
    conn = sqlite3.connect("inventario.db")
    c = conn.cursor()
    c.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    datos = c.fetchall()
    conn.close()
    return datos