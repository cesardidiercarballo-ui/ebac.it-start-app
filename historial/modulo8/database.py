import sqlite3

print(" * Importando módulo database.py")

DATABASE_NAME = "todolist.db"

def connect_db():
    conn = sqlite3.connect(DATABASE_NAME)
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
    try:
        conn.execute("ALTER TABLE tareas ADD COLUMN categoria TEXT NOT NULL DEFAULT 'General'")
    except sqlite3.OperationalError:
        pass
    conn.commit()
    print(" * Tabla tareas creada")
    return conn

if __name__ == "__main__":
    init_db()
