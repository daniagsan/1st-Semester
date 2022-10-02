#10 dado el sueldo de un empleado

sueldo = 0

sueldo = int(input("Ingrese su sueldo \n"))

if sueldo < 5000:
    sueldo += sueldo*0.15
    print("Su sueldo aumentará 15%: ", sueldo)
else:
    sueldo += sueldo*0.12
    print("Su sueldo aumentará 12%: ", sueldo)