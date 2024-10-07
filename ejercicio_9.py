# Identificar si al ingresar un numero este es múltiplo de 2, 3 o 5. Considerar que este número puede ser 
# múltiplos de las 2 o 3 opciones.
# GME0114 
# 29 de septiembre de 2024 
# Metodología de la Programación 
# Ledesma Lozada Leonardo 

num = int (input ("Ingrese un número: "))

prueba1 = num%2
prueba2 = num%3
prueba3 = num%5

if prueba1 == 0 :
    print ("El número ingresado es primo del 2.")
if prueba1 > 0 :
    print ("El número ingresado no es primo del 2.")

if prueba2 == 0 :
    print ("El número ingresado es primo del 3.")
if prueba2 > 0 :
    print ("El número ingresado no es primo del 3.")

if prueba1 == 0 :
    print ("El número ingresado es primo del 5.")
if prueba1 > 0 :
    print ("El número ingresado no es primo del 5.")