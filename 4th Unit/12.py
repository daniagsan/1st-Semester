#12.- Mostrar los números del 1 a N y su sumatoria.  

x=1
suma=0
n=0

print("Ingrese un número: ")
n=int(input())
print("---")

if n<0:
    for x in range(n,2):
        suma = suma + x
        print(x)
else:
    while x>0 and x<=n:
        suma = suma + x
        print(x)
        x+=1
    
print("\n","La sumatoria es: ", suma)