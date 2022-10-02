#10.- Mostrar la tabla del N con un For

i=1
n=0

print("Ingrese un número: ")
n=int(input())

for i in range(1,11):
    print(i,"x",n,"=",(n*i))