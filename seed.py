from database import connect_db, init_db

MINIMO_TAREAS = 10

TAREAS = [
    ("  Lavar ropa  ", "completada", "2026-09-01 09:00:00", "Hogar", "2026-09-02 20:00:00", "media", 60, "2026-09-01 10:20:00"),
    ("Hacer el súper", "completada", "2026-09-03 10:00:00", "compras", "2026-09-04 20:00:00", "Alta", 90, "2026-09-03 11:45:00"),
    ("Pagar la luz", "completada", "2026-09-05 08:00:00", "Personal", "2026-09-08 18:00:00", "alta", 15, "2026-09-10 09:00:00"),
    ("Hacer la comida", "completada", "2026-09-08 12:00:00", "Hogar", "2026-09-08 15:00:00", "urgente", 45, "2026-09-08 13:00:00"),
    ("Salir a correr", "completada", "2026-09-12 07:00:00", "Ejercicio", "pronto", "baja", 40, "2026-09-12 07:50:00"),
    ("Limpiar la cocina", "completada", "2026-09-15 18:00:00", "HOGAR ", "2026-09-16 20:00:00", " BAJA", -30, "2026-09-14 18:00:00"),
    ("Ir al banco", "pendiente", "2026-09-20 10:00:00", "Personal", "2026-09-25 14:00:00", "media", None, None),
    ("Pasear al perro", "pendiente", "2026-09-28 19:00:00", "Mascotas", "2026-10-10 20:00:00", "baja", 30, None),
]


def main():
    init_db()
    conn = connect_db()
    total = conn.execute("SELECT COUNT(*) FROM tareas").fetchone()[0]
    if total >= MINIMO_TAREAS:
        print(f" * La base ya tiene {total} tareas; no se insertó nada.")
        conn.close()
        return
    conn.executemany(
        """INSERT INTO tareas (titulo, estado, fecha_creacion, categoria, fecha_limite,
                               prioridad, tiempo_estimado, completado_en)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        TAREAS,
    )
    conn.commit()
    total = conn.execute("SELECT COUNT(*) FROM tareas").fetchone()[0]
    conn.close()
    print(f" * Se insertaron {len(TAREAS)} tareas. Total en la base: {total}")


if __name__ == "__main__":
    main()
