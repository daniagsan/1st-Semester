#13 Programa que pida cuatro numeros y diga cual es el mayor

n1=0
n2=0
n3=0
n4=0

n1 = int(input("Ingrese el 1er número \n"))
n2 = int(input("Ingrese el 2do número \n"))
n3 = int(input("Ingrese el 3er número \n"))
n4 = int(input("Ingrese el 4to número \n"))

if n1 > n2 and n1 > n3 and n1 > n4:
    print("El 1er número: ",n1," es mayor")
elif n2 > n1 and n2 > n3 and n2 > n4:
    print("El 2do número: ",n2," es mayor")
elif n3 > n1 and n3 > n2 and n3 > n4:
    print("El 3er número: ",n3," es mayor")
else:
    print("El 4to número: ",n4," es mayor")