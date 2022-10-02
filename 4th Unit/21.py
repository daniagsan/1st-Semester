#21.- Mostrar los números del N a 100 y su sumatoria While()

x=0
sumatoria=0

print("Ingrese un número: ")
x=int(input())

print("")

while x!=100:
    if x>=100:
        sumatoria=sumatoria+x
        print(x)
        x-=1
    else:
        sumatoria=sumatoria+x
        print(x)
        x+=1
        
sumatoria=sumatoria+x
        
print(x)
print("")
print("Sumatoria: ", sumatoria)