# Escribir un algoritmo en pseudocódigo que reciba un monto a pagar, le aplique un aumento del 20% por  
# IGV y finalmente un descuento de 5% sobre el nuevo valor, mostrando el monto original, el monto con  
# IGV y el monto con descuento en pantalla.  
# GME0114 
# 25 de septiembre de 2024 
# Metodología de la Programación 
# Ledesma Lozada Leonardo 
 
pago_Original = float ( input ( "Ingrese el pago original: " ) ) 
 
pago_IGV = pago_Original + (pago_Original * 0.2) 
pago_Descuento = pago_IGV - (pago_IGV * 0.05) 
 
print ("El pago original es de: ", pago_Original) 
print ("El pago original mas el IGV del 20 porciento es de: ", pago_IGV) 
print ("El pago IGV menos un descuento del 5 porciento es de: ", pago_Descuento) 