import random
from statistics import mode, median, mean

"""
1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 


edad = int(input("Ingrese su edad "))

if edad >= 18:
    print ("Es mayor de edad")

"""

"""
2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
mensaje “Desaprobado”. 


nota = int(input("Ingrese su nota "))

if nota >= 6:
    print ("Aprobado")

else:
    print ("Desaprobado")
"""

"""
3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
operador de módulo (%) en Python para evaluar si un número es par o impar.


numero = int(input("Ingrese un número par "))

if numero % 2 == 0:
    print ("Ha ingresado un número par")
else:
    print ("Por favor, ingrese un número par")
"""

"""
4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad "))

if edad < 12:
    print ("Pertenece a categoría: Niño/a.")

elif edad >= 12 and edad < 18: 
    print ("Pertenece a categoría: Adolescente.")

elif edad >= 18 and edad < 30:
    print ("Pertenece a categoría: Adulto/a joven.")

else:
    print ("Pertenece a categoría: Adulto/a.")
"""

"""
5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
como una lista o un string. 


contrasena = input("Ingrese su contraseña (entre 8 y 14 caracteres) ")

if  len(contrasena) >= 8 and len(contrasena) <= 14:
    print ("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
"""

"""
6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media 
y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. 
Imprimir el resultado por pantalla. 

# Creación de la lista de 50 números random.
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Variables para almacenar los resultados.
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Muestra la lista de número y los resultados de media, mediana, moda. 

print (numeros_aleatorios)
print (f"El promedio de todos los valores es {media}")
print (f"El valor central de los datos ordenados es {mediana}")
print (f"El valor más repetido {moda}")

# Condicional que compare para determinar el sesgo, si hay.
if media > mediana and mediana > moda:
    print ("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print ("Sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda:
    print ("Sin sesgo")
"""

"""
7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
pantalla.

# Se solicita una frase al usuario.
frase = input ("una frase o palabra ")

# Se guarda la última letra de la frase.
ultima_letra = frase[-1]

#  Si la última letra es vocal, se añade un signo de exclamación al final.
if (ultima_letra == "a" or 
    ultima_letra == "e" or 
    ultima_letra == "i" or 
    ultima_letra == "o" or 
    ultima_letra == "u"):
    
    frase_exclamacion = frase + "!" 
    print (frase_exclamacion)

# Si no, se imprime la frase tal cual fue ingresada.  
else:
    print (frase)
"""

"""
8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
dependiendo de la opción que desee: 
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
lower() y title() de Python para convertir entre mayúsculas y minúsculas. 


# Se solicita al usuario que ingrese su nombre.
nombre = input ("Ingrese su nombre ")

print ("1. Si quiere su nombre en mayúsculas.")
print ("2. Si quiere su nombre en minúsculas.")
print ("3. Si quiere su nombre con la primera letra mayúscula.")

# Se solicita al usuario que ingrese la opcion 1, 2 o 3.
opcion = int (input ("Ingrese la opción deseada "))
    
if opcion == 1:
        print (nombre.upper())
elif opcion == 2:
        print (nombre.lower())
elif opcion == 3:
        print (nombre.title())
# Si ingresa cualquier otro número, se vuelve a solicitar que ingrese opcion 1, 2 o 3.
else:
     opcion = input ("Ingrese solamente entre 1, 2 y 3 ")
"""

"""
9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
por pantalla: 
● Menor que 3: "Muy leve" (imperceptible). 
● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
generalmente no causa daños). 
● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
débiles). 
● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).


# Se solicita al usuario que escriba la magnitud de un terremoto.
magnitud = float (input ("Ingrese la magnitud "))

if magnitud < 3:
        print ("Muy leve. Imperceptible")
elif magnitud >= 3 and magnitud < 4:
        print ("Leve. Ligeramente perceptible")
elif magnitud >= 4 and magnitud < 5:
        print ("Moderado. Generalmente no causa daños")
elif magnitud >= 5 and magnitud < 6:
       print ("Fuerte. Puede causar daños en estructuras débiles")
elif magnitud >= 6 and magnitud < 7:
       print ("Muy Fuerte. Puede causar daños significativos")
elif magnitud >= 7:
       print ("Extremo. Puede causar graves daños a gran escala")
"""

"""
10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano. 

# Se solicita al usuario que ingrese en que hemisferio está.
hemisferio = input ("Ingrese el hemisferio (N/S) ")
hemisferio = hemisferio.upper()

# Se solicita que el mes del año en que se encuentra.
mes = int (input ("Ingrese el mes del año (1/12) "))

# Se solicita que día es.
dia = int (input ("Ingrese el dia (1/31) "))

# Condicional que evalua las estaciones del hemisferio Norte.
if hemisferio == "N" and ((mes == 12 and dia >= 21 ) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20)):
    print ("Usted se encuentra en Invierno")  
elif hemisferio == "N" and ((mes == 3 and dia > 21 ) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20)):
    print ("Usted se encuentra en Primavera")  
elif hemisferio == "N" and ((mes == 6 and dia > 21 ) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20)):
    print ("Usted se encuentra en Verano")
elif hemisferio == "N" and ((mes == 9 and dia > 21 ) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20)):
    print ("Usted se encuentra en Otoño")

# Condicional que evalua las estaciones del hemisferio Sur.
if hemisferio == "S" and ((mes == 12 and dia >= 21 ) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20)):
    print ("Usted se encuentra en Verano")  
elif hemisferio == "S" and ((mes == 3 and dia > 21 ) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20)):
    print ("Usted se encuentra en Otoño")  
elif hemisferio == "S" and ((mes == 6 and dia > 21 ) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20)):
    print ("Usted se encuentra en Invierno")
elif hemisferio == "S" and ((mes == 9 and dia > 21 ) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20)):
    print ("Usted se encuentra en Primavera")
"""