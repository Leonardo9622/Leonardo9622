# Ingrese el nombre de un alumno y las notas de su examen parcial, examen final y el promedio de prácticas; 
# muestre el nombre del alumno y su promedio final solo si el alumno está aprobado. Tenga en cuenta que 
# para el cálculo del promedio la nota del examen final tiene peso doble.
# GME0114 
# 29 de septiembre de 2024 
# Metodología de la Programación 
# Ledesma Lozada Leonardo 

nombre_alumnos = (input ("Ingrese el nombre del alumno: "))
promedio_practicas = float (input ("Ingrese el promedio de las practicas: "))
examen_parcial = float (input ("Ingrese la calificación del examen parcial: "))
examen_final = float (input ("Ingrese la calificación del examen final (Recuerde que este vale el doble): "))

promedio_final = (examen_parcial+(2*examen_final)+promedio_practicas)/3

print ("El alumno: ", str (nombre_alumnos), " tiene un promedio de: ", str (promedio_final))
if (promedio_final >= 7):
    print ("El alumno a sido aprovado.")

if (promedio_final < 7):
    print ("El alumno no a sido aprovado.")
