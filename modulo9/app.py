import os

from flask import Flask, jsonify, redirect, render_template, request

from database import init_db
from models import PRIORIDADES, Tarea

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "clave-local")
app.json.ensure_ascii = False
app.json.sort_keys = False

init_db()


@app.route("/")
def inicio():
    return redirect("/tareas")


@app.route("/tareas")
def mostrar_tareas():
    return render_template("tareas.html")


@app.route("/formulario")
def formulario():
    return render_template("formulario.html", categorias=Tarea.get_categorias(), prioridades=PRIORIDADES)


@app.route("/api/tareas", methods=["GET"])
def api_mostrar_tareas():
    return jsonify(Tarea.get_all())


@app.route("/api/tareas/<int:id>", methods=["GET"])
def api_obtener_tarea(id):
    tarea = Tarea.get_by_id(id)
    if tarea is None:
        return jsonify({"error": "La tarea no existe"}), 404
    return jsonify(tarea)


@app.route("/api/tareas", methods=["POST"])
def api_crear_tarea():
    try:
        Tarea.create(
            titulo=request.form.get("tarea"),
            categoria=request.form.get("categoria"),
            prioridad=request.form.get("prioridad"),
            fecha_limite=request.form.get("fecha_limite"),
            tiempo_estimado=request.form.get("tiempo_estimado"),
        )
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    return redirect("/tareas")


@app.route("/api/tareas/<int:id>/completar", methods=["PATCH"])
def api_completar_tarea(id):
    if Tarea.completar(id) == 0:
        return jsonify({"error": "La tarea no existe"}), 404
    return jsonify(Tarea.get_by_id(id))


@app.route("/api/tareas/<int:id>", methods=["DELETE"])
def api_eliminar_tarea(id):
    if Tarea.delete(id) == 0:
        return jsonify({"error": "La tarea no existe"}), 404
    return jsonify({"mensaje": "Tarea eliminada"})


@app.route("/api/protegido")
def api_protegido():
    clave = request.headers.get("X-Clave")
    if not clave or clave != app.config["SECRET_KEY"]:
        return jsonify({"error": "No autorizado"}), 401
    return jsonify({"mensaje": "Acceso concedido"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)