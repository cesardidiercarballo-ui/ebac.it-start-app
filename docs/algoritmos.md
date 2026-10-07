# Algoritmos de gestión de tareas

Diagramas de flujo de las operaciones del CRUD de Rutina.py: agregar, listar, actualizar y eliminar.

## 1. Agregar tarea

```mermaid
flowchart TD
    A([Usuario abre Nueva tarea]) --> B[Llena el formulario]
    B --> C[Envía el formulario a POST /api/tareas]
    C --> D{¿El nombre de la tarea tiene texto?}
    D -- No --> E[Responde error 400]
    D -- Sí --> F{¿Prioridad, fecha límite y tiempo son válidos?}
    F -- No --> E
    F -- Sí --> G[Guarda la tarea con estado pendiente]
    G --> H([Redirige a la lista Tareas])
    E --> I([Muestra el mensaje de error])
```

## 2. Listar tareas

```mermaid
flowchart TD
    A([Usuario abre /tareas]) --> B[Flask muestra la plantilla tareas.html]
    B --> C[app.js pide GET /api/tareas]
    C --> D[Consulta todas las tareas en SQLite]
    D --> E{¿La respuesta es correcta?}
    E -- No --> F([Muestra mensaje de error])
    E -- Sí --> G[Toma la siguiente tarea]
    G --> H{¿Está completada?}
    H -- Sí --> I[Muestra en verde, sin botón Completar]
    H -- No --> J[Muestra en amarillo, con botón Completar]
    I --> K[Muestra botón Eliminar]
    J --> K
    K --> L{¿Quedan tareas por mostrar?}
    L -- Sí --> G
    L -- No --> M([Lista terminada])
```

## 3. Actualizar tarea (completar)

```mermaid
flowchart TD
    A([Usuario pulsa Completar]) --> B[app.js envía PATCH /api/tareas/id/completar]
    B --> C{¿Existe la tarea?}
    C -- No --> D([Muestra mensaje de error 404])
    C -- Sí --> E[Cambia el estado a completada]
    E --> F[Guarda la fecha de completado]
    F --> G[Responde con la tarea actualizada]
    G --> H([app.js vuelve a cargar la lista])
```

## 4. Eliminar tarea

```mermaid
flowchart TD
    A([Usuario pulsa Eliminar]) --> B[app.js envía DELETE /api/tareas/id]
    B --> C{¿Existe la tarea?}
    C -- No --> D([Muestra mensaje de error 404])
    C -- Sí --> E[Borra la tarea de SQLite]
    E --> F[Responde Tarea eliminada]
    F --> G([app.js vuelve a cargar la lista])
```
