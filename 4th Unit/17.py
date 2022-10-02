#17.- Mostrar los números del 100 al N con un ciclo While()

x=0

print("Ingrese un número:")
x=int(input())
print("---")

while x!=100:
    if x>=100:
        print(x)
        x-=1
    else:
        print(x)
        x+=1
        
print(x)