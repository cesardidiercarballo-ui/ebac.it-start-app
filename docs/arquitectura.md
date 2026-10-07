# Arquitectura y navegación de Rutina.py

## Organización del proyecto

- `app.py`: rutas de Flask. Recibe las peticiones y devuelve las páginas.
- `models.py`: clase `Tarea`, con la validación de datos y las operaciones sobre las tareas.
- `database.py`: conexión a SQLite y creación de la tabla `tareas`.
- `templates/`: plantillas Jinja2. `layout.html` es la plantilla base y `tareas.html` y `formulario.html` la extienden.
- `static/app.js`: interactividad de la lista de tareas en el navegador.
- `todolist.db`: base de datos SQLite.
- `seed.py`: carga datos de ejemplo.

## Flujo entre pantallas

La aplicación tiene dos pantallas, accesibles desde la barra superior:

- **Tareas** (`/tareas`): muestra la lista de tareas pendientes y completadas.
- **Nueva tarea** (`/formulario`): muestra el formulario para agregar una tarea.

La ruta `/` redirige a `/tareas`.

Desde la pantalla **Tareas** se pueden completar o eliminar tareas. Desde la pantalla **Nueva tarea**, al enviar el formulario, la tarea se guarda y el usuario regresa a **Tareas**.
