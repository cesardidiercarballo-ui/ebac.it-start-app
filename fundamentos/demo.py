#indentacion / sangrado 
def saludar(nombre):
  print(f"Hola, {nombre}!") 

saludar("cesar") # asi se llama la funcion 

#variables mas comunes 
nombre = "cesar" #asi se define una variable tipo stringedad
edad = 25 #asi se define una variable tipo entero 
altura = 1.75 #asi se define una variable tipo flotante
completado = True # false    asi se define una variable tipo booleano|

print(nombre, edad, altura, completado) # asi se imprime una variable
#operaciones matematicas basicas
a = 10
b = 5   

suma = a + b
resta = a - b
multiplicacion = a * b  
division = a / b
potencia = a ** b
modulo = a % b
print(suma, resta, multiplicacion, division)


# concatenacion de cadenas de texto
print("la suma de  " + str(a) + " y " + str(b) + " es + " + str(suma)) # asi se concatenan cadenas de texto
