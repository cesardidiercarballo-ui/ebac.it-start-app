# Pseudocódigo del flujo principal

Describe las operaciones del CRUD de Rutina.py: agregar, listar, actualizar y eliminar.

## Agregar tarea

```
INICIO
  LEER titulo, categoria, prioridad, fecha_limite y tiempo_estimado desde el formulario
  QUITAR espacios al inicio y al final de titulo
  SI titulo está vacío ENTONCES
    RESPONDER error 400 "Falta el campo tarea"
  FIN SI
  SI categoria está vacía ENTONCES
    categoria = "General"
  FIN SI
  SI prioridad está vacía ENTONCES
    prioridad = "media"
  FIN SI
  SI prioridad no es "baja", "media" o "alta" ENTONCES
    RESPONDER error 400 "La prioridad debe ser: baja, media o alta"
  FIN SI
  SI fecha_limite no está vacía ENTONCES
    SI fecha_limite no tiene formato AAAA-MM-DD o AAAA-MM-DDTHH:MM ENTONCES
      RESPONDER error 400 "La fecha limite debe tener el formato AAAA-MM-DD o AAAA-MM-DDTHH:MM"
    FIN SI
    SI fecha_limite solo tiene fecha ENTONCES
      hora de fecha_limite = 23:59
    FIN SI
  SINO
    fecha_limite = vacía
  FIN SI
  SI tiempo_estimado no está vacío ENTONCES
    SI tiempo_estimado tiene algún carácter que no sea un dígito ENTONCES
      RESPONDER error 400 "El tiempo estimado debe ser un numero entero de minutos"
    FIN SI
    convertir tiempo_estimado a número entero
  SINO
    tiempo_estimado = vacío
  FIN SI
  GUARDAR la tarea con estado "pendiente" y la fecha de creación actual
  REDIRIGIR a /tareas
FIN
```

## Listar tareas

```
INICIO
  MOSTRAR la plantilla tareas.html
  PEDIR todas las tareas (GET /api/tareas)
  SI la respuesta no es correcta ENTONCES
    MOSTRAR "Error: no se pudieron cargar las tareas"
  FIN SI
  PARA CADA tarea en la lista, en orden de id, HACER
    SI el estado de la tarea es "completada" ENTONCES
      MOSTRAR la tarea en verde, sin botón Completar
    SINO
      MOSTRAR la tarea en amarillo, con botón Completar
    FIN SI
    MOSTRAR nombre, categoría, prioridad, fecha límite (o "sin fecha") y tiempo estimado (o "-")
    MOSTRAR botón Eliminar
  FIN PARA
FIN
```

## Actualizar tarea (editar)

```
INICIO
  RECIBIR el id de la tarea
  BUSCAR la tarea con ese id
  SI la tarea no existe ENTONCES
    RESPONDER error 404 "La tarea no existe"
  FIN SI
  MOSTRAR el formulario con los datos actuales de la tarea
  LEER titulo, categoria, prioridad, fecha_limite y tiempo_estimado desde el formulario
  VALIDAR los datos con las mismas reglas de "Agregar tarea"
  SI los datos no son válidos ENTONCES
    RESPONDER error 400 con el mensaje de validación
  FIN SI
  ACTUALIZAR la tarea con los nuevos datos
  SI no se actualizó ninguna tarea ENTONCES
    RESPONDER error 404 "La tarea no existe"
  FIN SI
  REDIRIGIR a /tareas
FIN
```

## Actualizar tarea (completar)

```
INICIO
  RECIBIR el id de la tarea
  BUSCAR la tarea con ese id
  SI la tarea no existe ENTONCES
    RESPONDER error 404 "La tarea no existe"
  FIN SI
  CAMBIAR el estado a "completada"
  GUARDAR la fecha de completado con la hora actual
  RESPONDER con la tarea actualizada
  VOLVER A CARGAR la lista de tareas
FIN
```

## Eliminar tarea

```
INICIO
  RECIBIR el id de la tarea
  BORRAR la tarea con ese id
  SI no se borró ninguna tarea ENTONCES
    RESPONDER error 404 "La tarea no existe"
  FIN SI
  RESPONDER "Tarea eliminada"
  VOLVER A CARGAR la lista de tareas
FIN
```
