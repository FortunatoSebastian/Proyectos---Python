import sqlite3
from datetime import datetime
import csv


QUERY_HISTORIAL = "SELECT * FROM historial"

def iniciar_db():
    conexion = sqlite3.connect("clima.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historial(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ciudad TEXT,
            temperatura REAL,
            descripcion TEXT,
            fecha TEXT
        )
    """)

    conexion.commit()
    conexion.close()

def guardar_consulta(ciudad, temperatura, descripcion):
    conexion = sqlite3.connect("clima.db")
    cursor = conexion.cursor()

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO historial (ciudad, temperatura, descripcion, fecha)
        VALUES (?, ?, ?, ?)
    """, (ciudad, temperatura, descripcion, fecha))

    conexion.commit()
    conexion.close()

def ver_historial():
    conexion = sqlite3.connect("clima.db")
    cursor = conexion.cursor()

    cursor.execute(QUERY_HISTORIAL)
    filas = cursor.fetchall()
    
    conexion.close()

    return filas

def exportar_historial():
    conexion = sqlite3.connect("clima.db")
    cursor = conexion.cursor()

    cursor.execute(QUERY_HISTORIAL)
    filas = cursor.fetchall()

    conexion.close()

    if not filas:
        print("No hay datos para exportar")
        return

    print(f"Se exportaron {len(filas)} registros")

    with open("historial_clima.csv", "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)

        writer.writerow(["ID", "Ciudad", "Temperatura", "Descripcion", "Fecha"])

        for fila in filas:
            writer.writerow([
                fila[0],
                fila[1],
                f"{fila[2]}°C",
                fila[3],
                fila[4],
            ])