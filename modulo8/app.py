from flask import Flask, render_template, jsonify
from database import init_db
from models import Tarea

app = Flask(__name__)

# Nos aseguramos de que la tabla exista antes de atender peticiones
init_db()

@app.route("/tareas")
def mostrar_tareas():
    tareas = Tarea.get_all()
    return render_template("tareas.html", tareas=tareas)

@app.route("/api/tareas", methods=["GET"])
def api_mostrar_tareas():
    return jsonify(Tarea.get_all())

if __name__ == "__main__":
    app.run(debug=True)