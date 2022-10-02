#17.-Una compañía de telefonía necesita un sistema con las propiedades necesarias para imprimir el costo de 
#una llamada telefónica, capturando la duración de la llamada en minutos y conociendo lo siguiente:

#1.- Toda llamada que dure tres minutos o menos tiene un costo de $5.

#2.- Cada minuto adicional cuesta $3

duracion_llamada=0
minuto_adicional=3
costo=0

print("Ingrese duración de la llamada: ",end="")
duracion_llamada = int(input())

if duracion_llamada > 3:
    costo = 5+((duracion_llamada-3)*minuto_adicional)
    
else:
    costo = 5

print("Ud. debe pagar: ",costo,"$" )