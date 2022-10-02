#18.-Una agencia de autos necesita un sistema con lo necesario para calcular el pago mensual para un agente de ventas de autos, 
#basándose en lo siguiente:

#El pago base es de $350, más una comisión de $15 por cada auto vendido y un bono de $40 si vendió más de 15 autos.

#El impuesto a pagar es el 5% del pago total.

#Los datos de entrada son el nombre del vendedor y el número de autos vendidos en el mes.

#Se desea imprimir el nombre del vendedor, el sueldo bruto, el impuesto y el sueldo neto.

autos_vendidos = 0
pago_base =  350
comision = 15
bono = 40
impuesto = 0.05
nombre =  []
sueldo_bruto = 0
sueldo_neto = 0

print("Ingrese su nombre: ",end="")
nombre = input()

print("Ingrese No. de autos vendidos: ",end="")
autos_vendidos = int(input())

sueldo_bruto = pago_base + (comision*autos_vendidos)

if autos_vendidos > 15:
    sueldo_bruto += bono

impuesto *= sueldo_bruto
sueldo_neto  = sueldo_bruto - impuesto

print("\nNombre: ",nombre,"\nSueldo Bruto: ",sueldo_bruto,"\nImpuesto: ",impuesto,"\nSueldo neto: ",sueldo_neto)