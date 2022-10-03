#28.-Se requiere determinar el costo que tendrá realizar una llamada telefónica con base en el tiempo que dura la llamada y en el costo por minuto.

costo = 0
tiempo = 0
minuto = 0

print("¿Cuántos minutos duró la llamada?: ",end="")
tiempo = int(input())

print("¿Cuál es el costo por minuto?: ",end="")
minuto = int(input())

costo = tiempo * minuto

print("El costo de la llamada es: ", costo)