#dado el sueldo de un empleado
sueldo = 0

sueldo = int(input("Ingrese su sueldo \n"))

if(sueldo<3000):
    sueldo += (sueldo*.15)
    print("Se le aplicará un aumento *ruidos de máquina* \n")
    print("Su sueldo ahora es ", sueldo)
else:
    print("Usted gana mucho dinero, pasese a front end")