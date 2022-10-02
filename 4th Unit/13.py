#13.- Realizar un programa que calcule el promedio de un alumno, 
#el "usuario" ingresará el número de materias y las calificaciones. Utilizando FOR

materias=0
n=1
promedio=0

print("Introduzca la cantidad de materias: ")
materias=int(input())

for x in range(0,materias):
    print("Introduzca el promedio de la materia numero",n,"")
    x=int(input())
    n+=1
    promedio += x
    
promedio = promedio/materias
print("Su promedio final es: ",promedio)