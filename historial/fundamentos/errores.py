#Debugging Errors

#sintax error


if 10 > 5:
    print("10 es mayor que 5")
else:
    print("10 no es mayor que 5")

#error de logica 
def es_par(numero): 
    return numero % 2 == 0
par = es_par(10)
print(f"el numero 10 es par?  {par}")

#errores de ejecucion
numeros = [1, 2, 3, 4, 5]
print(numeros[4])

#depuracion de errores

#esta funcion divide dos numeros y maneja el error de division por cero
def dividir(a, b):
    print(f"dividiendo {a} entre {b}")
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return 0
    

RESULTADO = dividir(10, 0)