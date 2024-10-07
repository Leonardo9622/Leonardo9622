# Problema 25: 
# Números Primos 
# Este algoritmo verifica si un número es primo, es decir, si solo es divisible por 1 y por sí mismo.
# GME0114 
# 01 de octubre de 2024 
# Metodología de la Programación 
# Ledesma Lozada Leonardo 

n = int (input ("Ingrese el númer a a evaluar: "))

contador = 2


if n <= 0:
    print ("Debe de ser un númer mayor a 0.")
if n > 1:
    while contador < n:
        residuo = n % contador
        
        if residuo == 0:
            print ("El número no es primo.")
            contador = n
        
        contador = contador + 1
    
    if residuo > 0:
        print ("El número es primo.")
