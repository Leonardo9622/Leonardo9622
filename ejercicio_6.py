# Elaborar un algoritmo que permita ingresar el nombre del trabajador, su sueldo básico y el número de 
# hijos, se deberá mostrar su bonificación y el sueldo final. Tenga en cuenta que la empresa está dando una 
# bonificación del 7% del sueldo básico sólo en el caso el trabajador tuviese hijos 
# GME0114 
# 26 de septiembre de 2024 
# Metodología de la Programación 
# Ledesma Lozada Leonardo 

bonidicacion = 0.07

nombre_trabajador = input ("Nombre del trabajador: ")
sueldo = float (input ("Sueldo base: "))
numero_hijos = int (input ("Ingrese el número de hijos: "))

if numero_hijos >= 1 :
    sueldo = sueldo + (sueldo * bonidicacion)

print ("El nombre del trabajado es: " + str (nombre_trabajador) + " Sueldo del trabajador: " + str (sueldo))