#8.- Mostrar los números del 100 al N con un ciclo For

n=0
i=0

print("Ingrese un número: ", end="")
n=int(input())
print("")

if n<100:
    rango=range(n,101)
else:
    rango=range(100,n+1)
    
for i in rango:
    print(i)
    i+=1