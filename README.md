# Rutina.py

Gestor de tareas personal desarrollado con Flask y SQLite como proyecto final del curso IT Start de EBAC.

## Enlaces

- Aplicación publicada: https://ebac-it-start-app-ntgn.onrender.com
- Repositorio: https://github.com/cesardidiercarballo-ui/ebac.it-start-app

## Descripción

Rutina.py permite registrar tareas con su categoría, prioridad, fecha límite y tiempo estimado, y gestionarlas desde una lista. La información se guarda en una base de datos SQLite.

## Funcionalidades

- Listar tareas con su categoría, prioridad, fecha límite y tiempo estimado.
- Agregar tareas desde un formulario.
- Editar los datos de una tarea.
- Marcar una tarea como completada.
- Eliminar una tarea.
- Consultar las tareas en formato JSON mediante la API.

## Tecnologías

| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3 |
| Servidor web | Flask 3.1.3 |
| Servidor de producción | Gunicorn |
| Plantillas | Jinja2 (incluido con Flask) |
| Base de datos | SQLite (módulo `sqlite3` de Python) |
| Estilos | Bootstrap 5.3.8, Bootstrap Icons 1.11.3 y hoja de estilos propia (`static/estilo.css`) |
| Interactividad | JavaScript (`fetch`) |
| Campo de categorías | Tom Select 2.3.1 |
| Despliegue | Render |

## Arquitectura

- `app.py`: rutas de Flask. Devuelve las páginas HTML y las respuestas de la API.
- `models.py`: clase `Tarea`, con la validación de datos y las operaciones sobre la base de datos.
- `database.py`: conexión a SQLite y creación de la tabla `tareas`.
- `templates/`: plantillas Jinja2. `layout.html` es la plantilla base.
- `static/app.js`: lista de tareas e interacciones en el navegador.
- `static/estilo.css`: estilos propios que complementan Bootstrap.
- `seed.py`: carga datos de ejemplo.

La documentación de la arquitectura, el mapa de sitio, los algoritmos y el pseudocódigo está en `docs/`.

## Modelo de datos

Tabla `tareas` en SQLite:

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | INTEGER | Identificador, se incrementa automáticamente. |
| `titulo` | TEXT | Nombre de la tarea. Obligatorio. |
| `estado` | TEXT | `pendiente` o `completada`. Por defecto `pendiente`. |
| `categoria` | TEXT | Categoría de la tarea. Por defecto `General`. |
| `prioridad` | TEXT | `baja`, `media` o `alta`. Por defecto `media`. |
| `fecha_creacion` | TEXT | Fecha y hora en que se creó la tarea. |
| `fecha_limite` | TEXT | Fecha y hora límite. Opcional. |
| `tiempo_estimado` | INTEGER | Minutos estimados. Opcional. |
| `completado_en` | TEXT | Fecha y hora en que se completó la tarea. Opcional. |

## Rutas y API

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/` | Redirige a `/tareas`. |
| GET | `/tareas` | Página con la lista de tareas. |
| GET | `/formulario` | Formulario para agregar una tarea. |
| GET | `/tareas/<id>/editar` | Formulario para editar una tarea. |
| GET | `/api/tareas` | Lista de tareas en JSON. |
| GET | `/api/tareas/<id>` | Una tarea en JSON. |
| POST | `/api/tareas` | Crea una tarea. |
| POST | `/api/tareas/<id>/editar` | Actualiza los datos de una tarea. |
| PATCH | `/api/tareas/<id>/completar` | Marca una tarea como completada. |
| DELETE | `/api/tareas/<id>` | Elimina una tarea. |
| GET | `/api/protegido` | Requiere el encabezado `X-Clave` con el valor de `SECRET_KEY`. |

Códigos de respuesta: 200 o 302 cuando la operación es correcta, 400 cuando los datos no son válidos, 401 cuando falta la clave en `/api/protegido` y 404 cuando la tarea no existe.

## Ejecución local

```
pip install -r requirements.txt
python seed.py
python app.py
```

Después abre `http://localhost:5000/tareas`.

El script `scripts/exportar_tareas.py` instala `pandas` automáticamente si no está disponible. El script `scripts/api_consumo.py` requiere `pandas` y `requests`, que no están en `requirements.txt`.

## Variables de entorno

| Variable | Uso | Valor por defecto |
|---|---|---|
| `SECRET_KEY` | Clave de la ruta `/api/protegido`. | `clave-local` |
| `PORT` | Puerto del servidor. | `5000` |

## Despliegue

La aplicación se publica en Render usando el `Procfile` (`web: gunicorn app:app`). Cada cambio enviado a la rama `main` activa un despliegue automático.

## Estructura del repositorio

- `app.py`, `models.py`, `database.py`, `seed.py`: código de la aplicación.
- `templates/`, `static/`: interfaz web.
- `data/`, `scripts/`, `notebooks/`: análisis de datos del módulo 9.
- `docs/`: documentación de la entrega.
- `historial/`: código de los módulos 5 a 8, como referencia. No forma parte de la aplicación.
