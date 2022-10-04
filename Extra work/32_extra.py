#32.-Se requiere determinar el sueldo semanal de un trabajador con base en las horas que trabaja y el 
#pago por hora que recibe, si el empleado trabaja más de 50 horas recibirá un bono del 25% pero si el 
#sueldo es mayor de 700 deberá pagar un impuesto por el 15%

sueldo_semanal = 0
horas_trabajadas = 0
pago_hora = 0
impuesto = 0.15
bono = 0.25

print("Horas trabajadas: ",end="")
horas_trabajadas = int(input())

print("\nPago por hora: ",end="")
pago_hora = int(input())

sueldo_semanal = pago_hora*horas_trabajadas

if horas_trabajadas > 50:
    sueldo_semanal += (sueldo_semanal*bono)
    print("Recibirá un bono del 25% por las horas trabajadas")

if sueldo_semanal > 700:
    sueldo_semanal -= (sueldo_semanal*impuesto)
    print("Por ganar más de 700, recibirá un impuesto del 15%")

print("Pago total: ",sueldo_semanal)