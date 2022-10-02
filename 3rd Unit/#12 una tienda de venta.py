#12 una tienda de venta
venta = 0

venta = int(input("Ingrese monto de venta: \n"))

if venta >= 500 and venta<=1000:
    venta -= venta*.5
elif venta >= 1000 and venta<=7000:
    venta -= venta*.11
elif venta >= 7000 and venta<=15000:
    venta -= venta*.18
elif venta >15000:
    venta -= venta*.25

print("El total a pagar es: ",venta,"$")