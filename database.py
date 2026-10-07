import os
import sqlite3

DATABASE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todolist.db")

COLUMNAS_NUEVAS = {
    "categoria": "TEXT NOT NULL DEFAULT 'General'",
    "fecha_limite": "TEXT",
    "prioridad": "TEXT NOT NULL DEFAULT 'media'",
    "tiempo_estimado": "INTEGER",
    "completado_en": "TEXT",
}


def connect_db():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = connect_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            estado TEXT NOT NULL DEFAULT 'pendiente',
            fecha_creacion TEXT NOT NULL DEFAULT (datetime('now','localtime'))
        )
    """)
    existentes = [fila["name"] for fila in conn.execute("PRAGMA table_info(tareas)")]
    for columna, definicion in COLUMNAS_NUEVAS.items():
        if columna not in existentes:
            conn.execute(f"ALTER TABLE tareas ADD COLUMN {columna} {definicion}")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print(" * Base de datos lista:", DATABASE_NAME)
