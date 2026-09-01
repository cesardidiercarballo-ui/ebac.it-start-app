from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/tareas")
def mostrar_tareas():
    tareas = [
    {   
            "nombre": "Hacer ejercicio",
            "estado": "pendiente",
            "prioridad": "alta",
            "fecha": "2026-08-27",
            "completada": False
        },

        {   "nombre": "Leer",
            "estado": "pendiente",
            "prioridad": "media",
            "fecha": "2026-08-28",
            "completada": False
        },

        {   "nombre": "Escribir",
            "estado": "pendiente",
            "prioridad": "baja",
            "fecha": "2026-08-29",
            "completada": True
         }
    ]    
    return render_template("tareas.html", tareas=tareas)
    
@app.route('/acerca-de')
def acerca_de():
    return render_template("acerca-de.html")

@app.route('/filtrar-tareas/<filtro>')
def filtro_etiqueta(filtro):
    return f"<h1>Filtro: {filtro}</h1>"

if __name__ == '__main__':
    app.run(debug=True)