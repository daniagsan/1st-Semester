#Obtener el mayor de 3 números

num1 = 0
num2 = 0
num3 = 0

num1 = int(input("Ingrese el 1er numero \n"))
num2 = int(input("Ingrese el 2do numero \n"))
num3 = int(input("Ingrese el 3er numero \n"))

if(num1>num2 and num1>num3):
    print("El ",num1," es mayor \n")
elif(num2>num1 and num2>num3):
    print("El ",num2," es mayor \n")
else:
    print("El ",num3," es mayor \n")

