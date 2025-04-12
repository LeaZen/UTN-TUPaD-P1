import random

"""
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

# Un ciclo for con un contador para el rango entre 0 y 100.
for contador in range (101):
    print (contador)

"""

"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene.

# Se solicita al usuario el ingreso del número entero.
numero = int (input("Ingrese un número entero "))

contador = 0
digito = abs(numero) # Por is ingresan un número negativo usamos abs.

if numero  == 0:
    contador += 1

while digito > 0: 
    digito = digito  // 10 # Buscamos la división exacta
    contador += 1 # El contador para los digitos.

print (contador)
"""

"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores.


# Se solicita al usuario el ingreso de dos números entero.
numero1 = int (input("Ingrese el primer número entero "))
numero2 = int (input("Ingrese el segundo número entero "))

acumulador = 0

# Con el ciclo for se cuenta desde el primer número hasta el segundo.
# Excluyendo los número ingresados.
for contador in range (numero1+1, numero2):
    acumulador += contador # Acá se suman los números.
    #print (contador)
print (f"La suma de los números comprendidos entre los ingresados es ", acumulador)
"""

"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0.

numeros = 1
acumulador = 0

while numeros > 0:
    # Se solicita al usuario que ingrese números enteros.
    numeros = int (input("Ingrese números enteros (para terminar ingrese 0) "))
    numeros = abs(numeros) # Por is ingresan un número negativo usamos abs.
    acumulador += numeros # Acá se suman los números.
   
print (f"La suma de los números es ", acumulador)
"""

"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

aleatorio = random.choice(range(10))
print (aleatorio)
acumulador = 0
numeros = 11

while numeros != aleatorio:
    # Se solicita al usuario que adivine el números.
    numeros = int (input("Adivine el número "))
    acumulador += 1 # Acá se suman los intentos.
   
print (f"Usted ha adivinado en", acumulador, "intentos")
"""

"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente. 

for numeros in range (100,-1, -2):
    
    print (numeros)
"""

"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario.

numero = int (input ("Ingrese un número positivo "))

calculo = 0
contador = 0
suma = 0

for calculo in range (numero): 
    contador += 1
    suma += calculo
    #print (contador, " ", numero)
    #print (calculo)
print (suma)
"""

"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

numero = 0
cont_pares = 0
cont_impares = 0
num_negativo = 0
num_positivo = 0

for i in range (1, 101):
       # print (i)
        numero = int (input ("Ingrese un número entero "))

        if numero > 0:
            num_positivo += 1
        elif numero < 0:
            num_negativo += 1

        if numero % 2 == 0:
            cont_pares += 1
        elif numero % 2 == 1:
            cont_impares += 1
        
print ( f"Hay ", cont_pares, "números pares")
print ( f"Hay ", cont_impares, "números impares")
print ( f"Hay ", num_negativo, "números negativos")
print ( f"Hay ", num_positivo, "números positivos")
"""

"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor).

numero = 0
suma = 0
media = 0

for i in range (1, 101):
        
        numero = int (input ("Ingrese un número entero "))
        suma += numero
        media = suma / i

print ( f"La media es ", media)
"""

"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 


numero = int (input ("Ingrese un número entero "))

ultimo_digito = 0
acumulador = "" 
div_exacta = 1 # Comienza con valor 1 para ingresar al While.

# El While funciona de acuerdo al valor de la división exacta del número ingresado.
while div_exacta > 0:
        
        div_exacta = numero // 10 # Se guarda la división exacta.
        ultimo_digito = int(numero % 10) # Se guarda el último dígito.
        #print (ultimo_digito)
        numero /= 10 # Se actualiza el valor del número.
        #print (numero)
        
        acumulador += str(ultimo_digito) # Aquí se acumulan los ultimos digitos.
        
print ( f"El número al revés es ", acumulador)
"""
