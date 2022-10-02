#13.- Realizar un programa que calcule el promedio de un alumno, el "usuario" ingresará el 
#número de materias y las calificaciones. Utilizando FOR

promedio=0
materias=0
calificacion=0
i=1

print("Ingrese el número de materias: ",end="")
materias=int(input())

for i in range(1,materias+1):
    print("Calificación",i," :",end="")
    calificacion=int(input())
    i+=1
    promedio += calificacion
    
print("El promedio es: ",(promedio/materias))