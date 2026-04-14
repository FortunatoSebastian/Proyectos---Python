import os
import sqlite3

conexion = sqlite3.connect("ventas.db")
cursor = conexion.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        producto TEXT,
        cantidad INTEGER,
        precio INTEGER,
        total INTEGER)
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventario(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        precio INTEGER)
""")

def agregar_producto():
    os.system("cls")
    nombre = input("Ingrese nombre del producto: ")
    precio = int(input("Ingrese el precio del producto: "))

    cursor.execute("INSERT INTO inventario (nombre, precio) VALUES (?, ?)", (nombre, precio))
    conexion.commit()

def registrar_venta():
    os.system("cls")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad que quiera comprar: "))

    cursor.execute("SELECT precio FROM inventario WHERE nombre = ?", (producto,))
    resultado = cursor.fetchone()
    
    if resultado is None:
        print("Erros: El producto no existe en el Inventario")
        input("\nPresione Enter para volver al menu...")
        return

    cursor.execute("INSERT INTO ventas (producto, cantidad, precio, total) VALUES (?, ?, ?, ?)", (producto, cantidad, resultado[0], cantidad * resultado[0]))
    conexion.commit()

def ver_inventario():
    os.system("cls")
    cursor.execute("SELECT * FROM inventario")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)
    input("\nPresione Enter para volver al menú...")

def ver_ventas():
    os.system("cls")
    cursor.execute("SELECT * FROM ventas")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)
    input("\nPresione Enter para volver al menú...")

def total_recaudado():
    os.system("cls")
    cursor.execute("SELECT producto, total FROM ventas")
    productos = cursor.fetchall()
    for fila in productos:
        print(f"{fila[0]}: ${fila[1]}")
    print("="*30)
    
    cursor.execute("SELECT SUM(total) FROM ventas")
    resultado = cursor.fetchone()
    print(f"Total recaudado: ${resultado[0]}")
    
    input("\nPresione Enter para volver al menú...")
    
def menu():
    while True:
        os.system("cls")
        print("="*30)
        print("   Sistemas de facturación")
        print("="*30)
        print("1 -Registrar Producto")
        print("2 -Registrar Venta")
        print("3 -Ver Ventas")
        print("4 -Ver Inventario")
        print("5 -Ver Total Recaudado")
        print("6 -Salir")
        opciones = input("\nIngrese la opcion deseada: ")
        match opciones:
            case "1":
                agregar_producto()
            case "2":
                registrar_venta()
            case "3":
                ver_ventas()
            case "4":
                ver_inventario()
            case "5":
                total_recaudado()
            case "6":
                print("Hasta luego!")
                break

menu()