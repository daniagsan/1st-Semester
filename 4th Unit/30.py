#30.- Mostrar un triangulo de 6 de altura al revés con un ciclo anidado

x=0

while x<6:
    y=6
    while y>x:
        print("*",end=" ")
        y-=1
    print("")
    x+=1