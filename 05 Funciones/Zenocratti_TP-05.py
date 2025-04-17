import math

"""
# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal

# Funciones-

def hola_mundo ():
    return print ("Hola Mundo")

# Programa Principal-

hola_mundo ()
"""

"""
# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

# Funciones-

def saludar_usuario (nombre):
    return print (f'"Hola {nombre}!”')

# Programa Principal-

nombre = input ("Ingrese su nombre ")
saludar_usuario(nombre)
"""

"""
# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Funciones-

def informacion_personal(nombre, apellido, edad, residencia): 
    return print (f'“Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}”')

# Programa Principal-

nombre = input ("Ingrese su nombre ")
apellido = input ("Ingrese su apellido ")
edad = input ("Ingrese su edad ")
residencia = input ("Ingrese su residencia ")

informacion_personal(nombre, apellido, edad, residencia)
"""

"""
# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro 
# y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva 
# el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# Funciones-

def calcular_area_circulo(radio):
    area = round (math.pi * (radio **2), 2)
    return area
    
def calcular_perimetro_circulo(radio):
    perimetro = round (math.pi * (radio*2), 2)
    return perimetro
    
# Programa Principal-

radio = float (input ("Ingrese el radio "))

print ( f"El perimetro es {calcular_perimetro_circulo(radio)} y el area es {calcular_area_circulo(radio)}")
"""

"""
# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y
# mostrar el resultado usando esta función.

# Funciones-

def segundos_a_horas(segundos):
    horas = round (segundos / 3600, 2)
    return horas 
    
# Programa Principal-

segundos = float (input ("Ingrese los segundos "))

print ( f"Los segundos ingresados equivalen a {segundos_a_horas(segundos)} horas ")
"""


"""
# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Funciones-

def tabla_multiplicar(numero):
    for i in range (1, 11):
     resultado = (numero * i)
     print (f"{numero} x {i} = {resultado}")
    
       
# Programa Principal-

numero = int (input ("Ingrese un número "))

tabla_multiplicar(numero)
"""

"""
# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado 
# de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

# Funciones-

def operaciones_basicas(a, b):
    
    suma = a + b 
    resta = a - b 
    multi = a * b
    division = round (a / b, 2)

    resultado_tupla = (suma, resta, multi, division)
    print (type(resultado_tupla))

    return print (f"La suma de los números es {resultado_tupla[0]}, su resta {resultado_tupla[1]}, La multiplicación {resultado_tupla[2]}, y la división {resultado_tupla[3]}" )
       
# Programa Principal-

operaciones_basicas(2, 7)
"""

"""
# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice demasa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función 
# para mostrar el resultado con dos decimales.

# Funciones-

def calcular_imc(peso, altura):
    imc = round (peso / altura ** 2, 2)
    return imc
    
# Programa Principal-

su_peso = float (input ("Ingrese su peso "))
su_altura = float (input ("Ingrese su altura "))

calcular_imc(su_peso, su_altura)

print ( f"El IMC es {calcular_imc(su_peso, su_altura)}")
"""

"""
# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# Funciones-

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Programa Principal-

celsius = float (input("Ingrese la temperatura en grados celsius "))

print ( f"La temperatura en fahrenheit es {celsius_a_fahrenheit(celsius)}")
"""

"""
# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

# Funciones-
def calcular_promedio(a, b, c):
    promedio = round ((a + b + c) / 3, 2)
    return promedio 

# Programa Principal-
notas = []
    
for i in range (1, 4):
     ingreso_nota = int (input(f"Ingrese la nota {i} "))
     notas.append(ingreso_nota)   

    #print ("Notas ingresadas:", notas)

print ("el promedio es ", calcular_promedio(notas[0], notas[1], notas[2]))
"""
