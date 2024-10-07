# Problema 18:
# Factorial de un Número 
# El factorial de un número es el producto de todos los números enteros positivos hasta ese número.
# GME0114 
# 01 de octubre de 2024 
# Metodología de la Programación 
# Ledesma Lozada Leonardo 

factorial = 1
contador = 1

numero = int(input("Ingrese el número para sacarle su factorial: "))

if numero < 0 :
    print ("No se puede calcilar el factorial de un número negativo.")
elif numero == 0:
    print ("El factorial de 0 es 1.")
else:
    while contador <= numero:
        factorial = factorial * contador
        contador = contador + 1
    print("El factorial de ", numero, " es: ", factorial)