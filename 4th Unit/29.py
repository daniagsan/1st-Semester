#29.- Mostrar un triangulo de 6 de altura con un ciclo anidado

x=0
y=0

while x<6:
    while y<x+1:
        print("*",end=" ")
        y+=1
    print("")
    y=0
    x+=1