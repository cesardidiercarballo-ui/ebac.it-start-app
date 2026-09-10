from database import connect_db

class Tarea:
    """Modelo de la tabla tareas: aqui viven las operaciones CRUD."""

    @staticmethod
    def create(titulo):
        conn = connect_db()
        cursor = conn.execute("INSERT INTO tareas (titulo) VALUES (?)", (titulo,))
        conn.commit()
        conn.close()
        return cursor.lastrowid

    @staticmethod
    def get_all():
        conn = connect_db()
        filas = conn.execute("SELECT * FROM tareas ORDER BY id").fetchall()
        conn.close()
        return filas
    
if __name__ == "__main__":
    nuevo_id = Tarea.create("Tarea creada desde el modelo")
    print(" * Tarea creada con id:", nuevo_id)
    for fila in Tarea.get_all():
        print(fila)

    