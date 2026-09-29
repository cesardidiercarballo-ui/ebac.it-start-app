from flask import Flask, render_template, jsonify
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

@app.route("/api/tareas/<int:id>", methods=["DELETE"])
def api_eliminar_tarea(id):
    Tarea.delete(id)
    return jsonify({"mensaje": "Tarea eliminada"})

if __name__ == "__main__":
    app.run(debug=True)