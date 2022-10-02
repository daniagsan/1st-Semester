#26.- Mostrar un cuadro de * de 10X10 con un ciclo anidado While

x=0
y=0

while x<10:
    while y<10:
        print("*",end=" ")
        y+=1
    print("")
    y=0
    x+=1