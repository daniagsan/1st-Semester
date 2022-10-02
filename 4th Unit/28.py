#28.- Mostrar un cuadro de NXN * con un ciclo anidado While

x=0
y=0

print("Ingrese el ancho:")
a=int(input())

print("Ingrese el largo:")
l=int(input())

while x<a:
    while y<l:
        print("*",end=" ")
        y+=1
    print("")
    y=0
    x+=1