#7.- Mostrar los números del N al 100 con un ciclo For

x=0
n=0
rango=[]

print("Introduzca un número: ")
n = int(input())
print("---")

if n>100:
    rango=range(100,n+1)
else:
    rango=range(n,101)
    
for x in rango:
    print(x)  