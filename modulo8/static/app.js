function cargarTareas() {
    fetch("/api/tareas")
        .then(function (respuesta) {
            return respuesta.json();
        })
        .then(function (tareas) {
            const lista = document.getElementById("lista-tareas");
            lista.innerHTML = "";
            tareas.forEach(function (tarea) {
                const color = tarea[2] === "completada" ? "list-group-item-success" : "list-group-item-warning";
                lista.innerHTML += `
                    <div class="list-group-item d-flex justify-content-between align-items-center ${color}">
                       <span class="fw-semibold">${tarea[1]} <span class="badge text-bg-secondary ms-2">${tarea[4]}</span></span>
                        <button class="btn btn-sm btn-outline-danger" onclick="eliminarTarea(${tarea[0]})">
                            <i class="bi bi-trash me-1"></i>Eliminar
                        </button>
                    </div>`;
            });
        });
}

function eliminarTarea(id) {
    fetch("/api/tareas/" + id, { method: "DELETE" })
        .then(function () {
            cargarTareas();
        });
}

cargarTareas();