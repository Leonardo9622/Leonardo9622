# Un vehículo viaja a una velocidad (V1 en Km/h) y deseamos saber en cuanto tiempo recorrerá una  
# distancia d (en Km). Mostar el tiempo en minutos. Adicionalmente mostrar la velocidad en (m/s)   
# GME0114 
# 24 de septiembre de 2024 
# Metodología de la Programación 
# Ledesma Lozada Leonardo 
 
v1 = float ( input ( "Ingresa la velocidad del vehiculo: " ) ) 
d = float ( input ( "Ingresa la distancia a recorrer: " ) )
 
tiempo_Kmh = d / v1 
tiempo_ms = tiempo_Kmh * 60 
velocidad_ms = v1 / 3.6 
 
print ("El tiempo en horas en que lo recorrera sera de: ", tiempo_Kmh, " h.") 
print ("El tiempo en minutos en que lo recorrera sera de: ", tiempo_ms, " m.") 
print ("La velocidad del vehiculo en m/s es: ", velocidad_ms, " m/s.") 