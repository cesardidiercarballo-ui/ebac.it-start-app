#funciones / entradas / salida

def saludar(nombre):
    print(f"hola {nombre}, ¿como estas?")

# llamada a una funcion 
saludar("juan")# 'juan' es un argumento 
saludar("maria")# 'maria' es un argumento 
saludar("pedro")# 'pedro' es un argumento 

def sumar(a, b):# 'a' y 'b' son parametros
    return a + b

resultado = sumar(10, 20)
print(resultado)

print("##################################################################################")
print("DEMO: ENTRADA Y SALIDA")

tareas = [] 

def mostrar_tareas():
    print("tareas pendientes:")
    for tarea in tareas:
        print(f"- {tarea}")

def agregar_tarea(): 
    tarea = input("ingresa la tarea: ")
    if tarea.strip() == "":
        print("no se puede agregar una tarea vacia")
        return
    tareas.append(tarea)
    print(f"tarea agregada: {tarea}")
    mostrar_tareas()


agregar_tarea()

