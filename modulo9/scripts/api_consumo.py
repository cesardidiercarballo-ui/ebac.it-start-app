import pandas as pd
import requests

URL_API = "http://127.0.0.1:5000/api/tareas"


def obtener_tareas(url=URL_API):
    try:
        respuesta = requests.get(url, timeout=5)
        respuesta.raise_for_status()
    except requests.exceptions.ConnectionError:
        raise SystemExit("No hay conexión con la API. Inicia el servidor con: python app.py")
    except requests.exceptions.RequestException as error:
        raise SystemExit(f"La API respondió con un error: {error}")
    return respuesta.json()


def main():
    tareas = obtener_tareas()
    df = pd.DataFrame(tareas)

    if df.empty:
        print("La API no devolvió tareas.")
        return

    pd.set_option("display.width", 160)
    pd.set_option("display.max_columns", None)

    print("=" * 60)
    print("RESUMEN DE TAREAS DESDE LA API")
    print("=" * 60)
    print(f"Número de registros: {len(df)}")
    print(f"Número de columnas:  {df.shape[1]}")
    print(f"Columnas: {', '.join(df.columns)}")
    print()
    print("Primeras 5 filas:")
    print(df.head())
    print()
    print("Tareas por estado:")
    print(df["estado"].value_counts().to_string())


if __name__ == "__main__":
    main()
