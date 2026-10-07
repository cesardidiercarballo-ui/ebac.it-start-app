const COLORES_PRIORIDAD = { alta: "text-bg-danger", media: "text-bg-warning", baja: "text-bg-info" };

function mostrarError(mensaje) {
    document.getElementById("alerta").innerHTML = `
        <div class="alert alert-danger" role="alert">
            ${mensaje}
        </div>`;
}

function formatearFecha(texto) {
    return texto ? texto.slice(0, 16) : "sin fecha";
}

function cargarTareas() {
    fetch("/api/tareas")
        .then(function (respuesta) {
            if (!respuesta.ok) {
                throw new Error("Error " + respuesta.status);
            }
            return respuesta.json();
        })
        .then(function (tareas) {
            const lista = document.getElementById("lista-tareas");
            lista.innerHTML = "";
            tareas.forEach(function (tarea) {
                const completada = tarea.estado === "completada";
                const color = completada ? "list-group-item-success" : "list-group-item-warning";
                const prioridad = (tarea.prioridad || "media").toLowerCase();
                const botonCompletar = completada ? "" : `
                    <button class="btn btn-sm btn-outline-success me-2" onclick="completarTarea(${tarea.id})">
                        <i class="bi bi-check2 me-1"></i>Completar
                    </button>`;
                lista.innerHTML += `
                    <div class="list-group-item d-flex justify-content-between align-items-center ${color}">
                        <div>
                            <span class="fw-semibold">${tarea.titulo}</span>
                            <span class="badge text-bg-secondary ms-2">${tarea.categoria}</span>
                            <span class="badge ${COLORES_PRIORIDAD[prioridad] || "text-bg-light"} ms-1">${prioridad}</span>
                            <div class="small text-muted">
                                Límite: ${formatearFecha(tarea.fecha_limite)}
                                · Estimado: ${tarea.tiempo_estimado ?? "-"} min
                            </div>
                        </div>
                        <div class="text-nowrap">
                            ${botonCompletar}
                            <a href="/tareas/${tarea.id}/editar" class="btn btn-sm btn-outline-primary me-2">
                                <i class="bi bi-pencil me-1"></i>Editar
                            </a>
                            <button class="btn btn-sm btn-outline-danger" onclick="eliminarTarea(${tarea.id})">
                                <i class="bi bi-trash me-1"></i>Eliminar
                            </button>
                        </div>
                    </div>`;
            });
        })
        .catch(function () {
            mostrarError("Error: no se pudieron cargar las tareas");
        });
}

function completarTarea(id) {
    fetch("/api/tareas/" + id + "/completar", { method: "PATCH" })
        .then(function (respuesta) {
            if (!respuesta.ok) {
                throw new Error("Error " + respuesta.status);
            }
            cargarTareas();
        })
        .catch(function () {
            mostrarError("Error: no se pudo completar la tarea");
        });
}

function eliminarTarea(id) {
    fetch("/api/tareas/" + id, { method: "DELETE" })
        .then(function (respuesta) {
            if (!respuesta.ok) {
                throw new Error("Error " + respuesta.status);
            }
            cargarTareas();
        })
        .catch(function () {
            mostrarError("Error: no se pudo eliminar la tarea");
        });
}

cargarTareas();
