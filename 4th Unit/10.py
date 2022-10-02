#10.- Mostrar la tabla del N con un For
n=0
print("La tabla del n \nIntroduzca un número: ")
n=int(input())
print("---")
for x in range(n,n*10+1,n):
    print(x)
else:
    print("\n Se terminó el programa")