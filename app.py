from flask import Flask, make_response, redirect, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/nueva-tarea', methods=['GET', 'POST'])
def nueva_tarea():
    if request.method == 'POST':
        nombre = request.form['title']
        #return redirect("/tareas")
        tareas = request.cookies.get('tareas', "")
        #Ej: cookies: tareas=Hacer ejercicio,Leer,Escribir
        lista_tareas = tareas.split(",") if tareas else []
        #Ej: lista_tareas = ["Hacer ejercicio", "Leer", "Escribir"]
        lista_tareas.append(nombre)
        response = make_response(redirect("/tareas"))
        #Ej:cookies: tareas= "Hacer ejercicio,Leer,Escribir,Nueva tarea"
        response.set_cookie('tareas', ",".join(lista_tareas))
        return response
    return render_template("formulario.html")

@app.route("/tareas")
def mostrar_tareas():
    # Tareas de ejemplo (informacion base)
    tareas_base = [
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

    # Tareas agregadas desde el formulario (guardadas en la cookie)
    tareas = request.cookies.get('tareas', "")
    lista_tareas = tareas.split(",") if tareas else []
    for nombre in lista_tareas:
        tareas_base.append({
            "nombre": nombre,
            "estado": "pendiente",
            "prioridad": "media",
            "fecha": "",
            "completada": False
        })

    return render_template("tareas.html", tareas=tareas_base)

@app.route('/acerca-de')
def acerca_de():
    return render_template("acerca-de.html")

@app.route('/filtrar-tareas/<filtro>')
def filtro_etiqueta(filtro):
    return f"<h1>Filtro: {filtro}</h1>"

if __name__ == '__main__':
    app.run(debug=True)