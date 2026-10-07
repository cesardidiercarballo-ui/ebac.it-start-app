# Errores y troubleshooting - Módulo 10

URL pública: https://ebac-it-start-app-ntgn.onrender.com

Copia del log de Render: `docs/m10/log-render.txt`

## Revisión de logs

Se navegaron todas las rutas de la app en Render (`/`, `/tareas`, `/formulario`, `/api/tareas`, `/api/tareas/1`, `/api/tareas/9999`, `/api/protegido`). Los logs no muestran errores de ejecución: solo respuestas `200`, `302` y `304`.

Las respuestas `404` en `/api/tareas/9999` y `401` en `/api/protegido` son intencionales. La app las devuelve cuando la tarea no existe o cuando falta la clave. El `404` de `/favicon.ico` ocurre porque la app no tiene ícono.

## Error 1: Render no encuentra repositorios

- **Descripción:** Al crear el Web Service, Render mostró "No repositories found".
- **Causa:** Render solo tenía la identidad de la cuenta de GitHub, pero no permiso para ver los repositorios.
- **Solución:** Se instaló la app de Render en GitHub desde el botón "GitHub" de la pantalla y se seleccionó el repositorio `ebac.it-start-app`.

## Error 2: Git no puede crear index.lock

- **Descripción:** Al ejecutar `git add modulo9` apareció `fatal: Unable to create '.git/index.lock': File exists`.
- **Causa:** Quedó un archivo de bloqueo `.git/index.lock` de otro proceso de Git.
- **Solución:** Se eliminó el archivo `.git/index.lock` y se repitió `git add modulo9`.

## Estructura: la app está dentro de `modulo9`

- **Descripción:** La app, el `Procfile` y el `requirements.txt` están en la carpeta `modulo9`, no en la raíz del repositorio.
- **Causa:** Por defecto Render busca esos archivos en la raíz del repositorio.
- **Solución:** En el Web Service se configuró **Root Directory** como `modulo9`. Por eso los cambios que deben activar el despliegue automático se hacen dentro de `modulo9`.
