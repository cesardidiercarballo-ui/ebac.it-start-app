from database import connect_db

class Tarea:
    """Modelo de la tabla tareas: aqui viven las operaciones CRUD."""

    @staticmethod
    def create(titulo, categoria="General"):
        conn = connect_db()
        cursor = conn.execute("INSERT INTO tareas (titulo, categoria) VALUES (?, ?)", (titulo, categoria))
        conn.commit()
        conn.close()
        return cursor.lastrowid

    @staticmethod
    def get_all():
        conn = connect_db()
        filas = conn.execute("SELECT * FROM tareas ORDER BY id").fetchall()
        conn.close()
        return filas

    @staticmethod
    def get_by_id(tarea_id):
        conn = connect_db()
        fila = conn.execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,)).fetchone()
        conn.close()
        return fila

    @staticmethod
    def delete(tarea_id):
        conn = connect_db()
        cursor = conn.execute("DELETE FROM tareas WHERE id = ?", (tarea_id,))
        conn.commit()
        conn.close()
        return cursor.rowcount

    @staticmethod
    def get_categorias():
        conn = connect_db()
        filas = conn.execute("SELECT DISTINCT categoria FROM tareas ORDER BY categoria").fetchall()
        conn.close()
        categorias = []
        for fila in filas:
            categorias.append(fila[0])
        return categorias
    
if __name__ == "__main__":
    nuevo_id = Tarea.create("Tarea creada desde el modelo")
    print(" * Tarea creada con id:", nuevo_id)
    for fila in Tarea.get_all():
        print(fila)

