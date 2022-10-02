#12.- Mostrar los números del 1 a N y su sumatoria.

n=0
x=0
suma=0
rango=[]


print("Introduzca un número: ")
n=int(input())

if n>0:
    rango=range(1,n+1)
else:
    rango=range(n,2)
    
for x in rango:
    print(x)
    suma += x

print("La sumatoria es: ",suma)

