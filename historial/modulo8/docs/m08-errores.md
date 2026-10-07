# Errores comunes entre frontend y backend (Módulo 8)

## 1. 404 Not Found al abrir 127.0.0.1:5000/
- Causa: la app no tiene una ruta para `/`.
- Solución: abrir una ruta que exista, como `/tareas` o `/api/tareas`.

## 2. ERR_CONNECTION_REFUSED
- Causa: el servidor Flask está apagado.
- Solución: ejecutar `python app.py` dentro de la carpeta `modulo8`.

## 3. IndentationError
- Causa: una línea con más o menos espacios que el resto de su bloque, por ejemplo `@staticmethod` con 5 espacios.
- Solución: usar 4 espacios por cada nivel de sangría.

## 4. AttributeError: 'tuple' object has no attribute 'to_dict'
- Causa: `get_all()` devuelve tuplas de SQLite, que no tienen `to_dict()`.
- Solución: devolver `jsonify(Tarea.get_all())` directamente.

## 5. Los cambios no se reflejan
- Causa: el archivo no se guardó.
- Solución: guardar con Ctrl+S. Con `debug=True`, Flask se reinicia solo al guardar.

## 6. 400 Bad Request al crear una tarea
- Causa: la petición llega sin el campo `tarea`.
- Solución: enviar el campo `tarea`. El formulario usa `required` para evitarlo.

## 7. 404 Not Found al eliminar una tarea
- Causa: el id de la tarea no existe.
- Solución: verificar que el id exista. La API responde `{"error": "La tarea no existe"}`.

## 8. La página no avisa cuando falla una petición
- Causa: `fetch` no falla con un 400 o 404, solo cuando no hay conexión con el servidor.
- Solución: revisar `respuesta.ok`, lanzar un error con `throw new Error(...)` y mostrarlo con `mostrarError` dentro del `.catch()`.

## 9. git: Unable to create '.git/index.lock'
- Causa: quedó un archivo de bloqueo de un proceso de Git anterior.
- Solución: cerrar otros procesos de Git y borrar el archivo `.git/index.lock`.

## 10. git: pathspec 'modulo8' did not match any files
- Causa: la terminal ya estaba dentro de la carpeta `modulo8`.
- Solución: usar `git add .` o subir a la raíz del repositorio.