#6.- Mostrar los números del 1 al N con un ciclo For


x=0
n=0
rango=[]

print("Introduzca un número: ")
n = int(input())
print("---")

if n<0:
    rango=range(n,2)
else:
    rango=range(1,n+1)
    
for x in rango:
    print(x)