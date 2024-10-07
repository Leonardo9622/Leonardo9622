# Problema 18:
# Factorial de un Número 
# El factorial de un número es el producto de todos los números enteros positivos hasta ese número.
# GME0114 
# 01 de octubre de 2024 
# Metodología de la Programación 
# Ledesma Lozada Leonardo 

n = int (input ("¿Cúantos números de Fibonacci deseas generar? "))

contador = 0
a = 0
b = 1

if n <= 0 :
    print ("Debes ingresar un número mayor que 0.")
elif n == 1:
    print ("0")
else:
    while contador <= n:
        fibonacci = a + b
        a = b
        b = fibonacci
        contador = contador + 1
        print (fibonacci)