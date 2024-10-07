# Problema 29: 
# Generar una Tabla de Multiplicar 
# Este algoritmo genera la tabla de multiplicar de un número hasta 10
# GME0114 
# 01 de octubre de 2024 
# Metodología de la Programación 
# Ledesma Lozada Leonardo 

n = int (input ("Ingrese de que  número desea hacer la tabla de multiplicar: "))

contador = 1

while contador <= 10 :
    tabla = contador * n
    print (contador, " x ", n, " = ", tabla)
    contador = contador + 1