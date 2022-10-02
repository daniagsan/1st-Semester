#20.- Mostrar los números del N a M

n=0
m=0

print("Ingrese dos números: ")
n=int(input())
m=int(input())

print("---")

if n>m:
    x=m
    m=n
    n=x
    
while n<m:
    print(n)
    n+=1

print(m)