# Rutina.py

Gestor de tareas personal desarrollado con Flask y SQLite como proyecto final del curso IT Start (EBAC).

## Funcionalidades

- Listar tareas con su categoría, prioridad, fecha límite y tiempo estimado.
- Crear tareas desde un formulario con Bootstrap.
- Marcar tareas como completadas.
- Eliminar tareas.
- API REST en `/api/tareas` que responde en JSON.
- Ruta protegida `/api/protegido` que valida la variable `SECRET_KEY` mediante el encabezado `X-Clave`.

## Tecnologías

Python, Flask, SQLite, Jinja2, Bootstrap 5, JavaScript y Gunicorn.

## Estructura

- `app.py`, `database.py`, `models.py`: backend, conexión y modelo de datos.
- `templates/`, `static/`: interfaz web.
- `seed.py`: carga de datos de ejemplo.
- `data/`, `scripts/`, `notebooks/`: análisis de datos del módulo 9.
- `docs/`: documentación de la entrega (errores, despliegue y entrega final).
- `historial/`: código de los módulos 5 a 8, solo como referencia. No forma parte de la aplicación.

## Ejecución local

```
pip install -r requirements.txt
python seed.py
python app.py
```

Después abre `http://localhost:5000/tareas`.

## Despliegue

La aplicación se publica en Render con `Procfile` (`web: gunicorn app:app`). Cada cambio en la rama `main` activa un despliegue automático.

## Enlaces

- Aplicación: https://ebac-it-start-app-ntgn.onrender.com
- Repositorio: https://github.com/cesardidiercarballo-ui/ebac.it-start-app
