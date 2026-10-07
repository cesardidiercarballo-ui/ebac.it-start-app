import os
import sqlite3

import pandas as pd

CARPETA_MODULO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_DB = os.path.join(CARPETA_MODULO, "todolist.db")
CARPETA_DATA = os.path.join(CARPETA_MODULO, "data")


def main():
    if not os.path.exists(RUTA_DB):
        raise SystemExit(f"No se encontró la base de datos en {RUTA_DB}. Ejecuta primero: python seed.py")

    conn = sqlite3.connect(RUTA_DB)
    df = pd.read_sql_query("SELECT * FROM tareas ORDER BY id", conn)
    conn.close()
    df["tiempo_estimado"] = df["tiempo_estimado"].astype("Int64")

    os.makedirs(CARPETA_DATA, exist_ok=True)
    ruta_csv = os.path.join(CARPETA_DATA, "tareas.csv")
    ruta_json = os.path.join(CARPETA_DATA, "tareas.json")
    df.to_csv(ruta_csv, index=False, encoding="utf-8")
    df.to_json(ruta_json, orient="records", force_ascii=False, indent=2)

    print(f" * {len(df)} tareas exportadas")
    print(f"   - {ruta_csv}")
    print(f"   - {ruta_json}")


if __name__ == "__main__":
    main()
