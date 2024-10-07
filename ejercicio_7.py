# Desarrolle un algoritmo que solicite 3 números correspondientes a los lados de un triángulo rectángulo 
# (considere que los valores ingresados si forman un triángulo rectángulo) e indique cuál de los valores 
# ingresados corresponde a la hipotenusa. 
# GME0114 
# 27 de septiembre de 2024 
# Metodología de la Programación 
# Ledesma Lozada Leonardo 

import math

x = float (input ("Ingrese el valor de x: "))
y = float (input ("Ingrese el valor de y: "))
z = float (input ("Ingrese el valor de z: "))

h1 = math.sqrt (math.pow (x, 2) + math.pow (y, 2))
h2 = math.sqrt (math.pow (y, 2) + math.pow (z, 2))
h3 = math.sqrt (math.pow (x, 2) + math.pow (z, 2))

if h1 == z :
    print ("El valor de z: " + str (z) + " es la hipotenusa.")

if h1 == x :
    print ("El valor de z: " + str (x) + " es la hipotenusa.")

if h1 == y :
    print ("El valor de z: " + str (y) + " es la hipotenusa.")