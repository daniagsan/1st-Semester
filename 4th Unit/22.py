#22.- Realizar un programa que calcule el promedio de un alumno, 
#el "usuario" ingresará el número de materias y las calificaciones. Utilizando un While

calif=0
promedio=0
materias=0
x=0

print("Ingrese cantidad de materias: ")
materias=int(input())

while x!=materias:
    x+=1
    print("Calificación materia",x)
    calif=int(input())
    promedio+=calif
    
promedio/=materias

print("Su promedio es:", promedio)