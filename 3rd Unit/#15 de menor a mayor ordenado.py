#3 numeros de menor a mayor

n1=0
n2=0
n3=0

n1=(input('Ingrese el 1er numero: '))
n2=(input('Ingrese el 2do numero: '))
n3=(input('Ingrese el 3er numero: '))
#print(n1,n2,n3)
if n1<n2 and n2<n3:
    print(n1,n2,n3)
elif n1<n3 and n3<n2:
    print(n1,n3,n2)
elif n3<n2 and n2<n1:
    print(n3,n2,n1)
elif n3<n2 and n2<n1:
    print(n3,n2,n1)
elif n3<n1 and n1<n2:
    print(n3,n1,n2)
elif n2<n3 and n3<n1:
    print(n2,n3,n1)
elif n2<n1 and n1<n3:
    print(n2,n1,n3)