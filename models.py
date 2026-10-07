from datetime import datetime

from database import connect_db

PRIORIDADES = ["baja", "media", "alta"]

COLUMNAS = """id, titulo, estado, categoria, prioridad, fecha_creacion,
              fecha_limite, tiempo_estimado, completado_en"""


class Tarea:
    """Modelo de la tabla tareas con los campos extendidos del modulo 9."""

    @staticmethod
    def to_dict(fila):
        return dict(fila) if fila is not None else None

    @staticmethod
    def validate(titulo, categoria, prioridad, fecha_limite, tiempo_estimado):
        titulo = (titulo or "").strip()
        if titulo == "":
            raise ValueError("Falta el campo tarea")

        categoria = (categoria or "").strip() or "General"

        prioridad = (prioridad or "media").strip().lower()
        if prioridad not in PRIORIDADES:
            raise ValueError("La prioridad debe ser: baja, media o alta")

        fecha_limite = (fecha_limite or "").strip()
        if fecha_limite:
            try:
                fecha = datetime.fromisoformat(fecha_limite)
            except ValueError:
                raise ValueError("La fecha limite debe tener el formato AAAA-MM-DD o AAAA-MM-DDTHH:MM")
            if len(fecha_limite) == 10:
                fecha = fecha.replace(hour=23, minute=59)
            fecha_limite = fecha.strftime("%Y-%m-%d %H:%M:%S")
        else:
            fecha_limite = None

        tiempo = str(tiempo_estimado if tiempo_estimado is not None else "").strip()
        if tiempo:
            if not tiempo.isdigit():
                raise ValueError("El tiempo estimado debe ser un numero entero de minutos")
            tiempo = int(tiempo)
        else:
            tiempo = None

        return titulo, categoria, prioridad, fecha_limite, tiempo

    @staticmethod
    def create(titulo, categoria="General", prioridad="media", fecha_limite=None, tiempo_estimado=None):
        datos = Tarea.validate(titulo, categoria, prioridad, fecha_limite, tiempo_estimado)
        conn = connect_db()
        cursor = conn.execute(
            """INSERT INTO tareas (titulo, categoria, prioridad, fecha_limite, tiempo_estimado)
               VALUES (?, ?, ?, ?, ?)""",
            datos,
        )
        conn.commit()
        conn.close()
        return cursor.lastrowid

    @staticmethod
    def get_all():
        conn = connect_db()
        filas = conn.execute(f"SELECT {COLUMNAS} FROM tareas ORDER BY id").fetchall()
        conn.close()
        resultado = []
        for fila in filas:
            resultado.append(Tarea.to_dict(fila))
        return resultado

    @staticmethod
    def get_by_id(tarea_id):
        conn = connect_db()
        fila = conn.execute(f"SELECT {COLUMNAS} FROM tareas WHERE id = ?", (tarea_id,)).fetchone()
        conn.close()
        return Tarea.to_dict(fila)

    @staticmethod
    def completar(tarea_id):
        conn = connect_db()
        cursor = conn.execute(
            """UPDATE tareas
               SET estado = 'completada', completado_en = datetime('now','localtime')
               WHERE id = ?""",
            (tarea_id,),
        )
        conn.commit()
        conn.close()
        return cursor.rowcount

    @staticmethod
    def actualizar(tarea_id, titulo, categoria, prioridad, fecha_limite, tiempo_estimado):
        datos = Tarea.validate(titulo, categoria, prioridad, fecha_limite, tiempo_estimado)
        conn = connect_db()
        cursor = conn.execute(
            """UPDATE tareas
               SET titulo = ?, categoria = ?, prioridad = ?, fecha_limite = ?, tiempo_estimado = ?
               WHERE id = ?""",
            (*datos, tarea_id),
        )
        conn.commit()
        conn.close()
        return cursor.rowcount

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
        return [fila["categoria"] for fila in filas]
