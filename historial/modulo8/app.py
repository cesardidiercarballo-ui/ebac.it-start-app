from flask import Flask, render_template, jsonify, request, redirect
from database import init_db
from models import Tarea

app = Flask(__name__)

init_db()

@app.route("/tareas")
def mostrar_tareas():
    tareas = Tarea.get_all()
    return render_template("tareas.html", tareas=tareas)

@app.route("/api/tareas", methods=["GET"])
def api_mostrar_tareas():
    return jsonify(Tarea.get_all())

@app.route("/api/tareas/<int:id>", methods=["GET"])
def api_obtener_tarea(id):
    tarea = Tarea.get_by_id(id)
    if tarea is None:
        return jsonify({"error": "La tarea no existe"}), 404
    return jsonify(tarea)

@app.route("/api/tareas/<int:id>", methods=["DELETE"])
def api_eliminar_tarea(id):
    borradas = Tarea.delete(id)
    if borradas == 0:
        return jsonify({"error": "La tarea no existe"}), 404
    return jsonify({"mensaje": "Tarea eliminada"})

@app.route("/formulario")
def formulario():
    categorias = Tarea.get_categorias()
    return render_template("formulario.html", categorias=categorias)

@app.route("/api/tareas", methods=["POST"])
def api_crear_tarea():
    titulo = request.form.get("tarea", "").strip()
    categoria = request.form.get("categoria", "").strip()
    print("Datos recibidos:", titulo, categoria)
    if titulo == "":
        return jsonify({"error": "Falta el campo tarea"}), 400
    if categoria == "":
        categoria = "General"
    Tarea.create(titulo, categoria)
    return redirect("/tareas")

if __name__ == "__main__":
    app.run(debug=True)