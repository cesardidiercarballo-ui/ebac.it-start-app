#Estucturas de control
tarea = "leer" 
if tarea == "leer":
    print("suerte con tu tarea")
else:
    print("suerte en la ejecución de tu tarea")


tareas = ["hacer ejercicio", "leer", "escribir"]

print("##################################################################################")
print("DEMO: BUCLE FOR")
print("##################################################################################")
for tarea in tareas:
    print(f"la tarea es: {tarea}")

    print("##################################################################################")
print("DEMO: BUCLE WHILE")
print("##################################################################################")

contador = 0


while contador < 10:
    print(f"contador: {contador}")
    contador += 1

   