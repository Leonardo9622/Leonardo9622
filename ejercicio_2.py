# Diseñar un algoritmo que pida el total de kilómetros recorridos, el precio de la gasolina (por litro), el  
# dinero de gasolina gastada en el viaje y el tiempo que se ha tardado (en horas y minutos) y que calcule: 
# - Consumo de gasolina (en litros y euros) por cada 100 km  
# - Consumo de gasolina (en litros y euros) por cada km  
# - Velocidad media (en km/h y m/s) 
# GME0114 
# 25 de septiembre de 2024 
# Metodología de la Programación 
# Ledesma Lozada Leonardo 
 
kilometros_recorridos = float ( input ( "Ingresa el total de kilometros recorridos: " ) ) 
precio_gasolina= float ( input ( "Ingresa el precio de la gasolina: " ) ) 
gasto_gasolina = float ( input ( "Ingresa el gasto por la gasolina: " ) ) 
tiempo_horas = float ( input ( "Ingresa el tiempo del recorrido en horas: " ) ) 
tiempo_minutos = float ( input ( "Ingresa el tiempo del recorrido en minutos (Si es necesario): " ) ) 
 
gasolina_gastados = gasto_gasolina / precio_gasolina 
gasolina_por_100km = (gasolina_gastados / kilometros_recorridos) * 100 
gasto_por_100km = (gasto_gasolina / kilometros_recorridos) * 100 
gasolina_por_km = gasolina_gastados / kilometros_recorridos 
gasto_por_km = gasto_gasolina / kilometros_recorridos 
tiempo_total_horas = tiempo_horas + (tiempo_minutos / 60) 
velocidad_kmh = kilometros_recorridos / tiempo_total_horas 
velocidad_ms = (velocidad_kmh * 1000) / 3600 

print (" ") 
print ("Respuesta: ") 
print ("Consumo por cada 100 km en litros: ", gasolina_por_100km, " l." ) 
print ("Costo por cada 100 km: ", gasto_por_100km) 
print (" ")  
print ("Consumo por cada km en litros: ", gasolina_por_km, " l." ) 
print ("Costo por cada km: ", gasto_por_km) 
print (" ") 
print ("Velocidad media en km/h: ", velocidad_kmh, " km/h.") 
print ("Velocidad media en m/s: ", velocidad_ms, " m/s.") 