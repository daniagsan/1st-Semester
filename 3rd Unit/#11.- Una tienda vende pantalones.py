#11.- Una tienda vende pantalones

preciopantalon = 200
cantidad = 0
total = 0

cantidad = int(input("¿Cuántos pantalones compró? \n"))

if cantidad < 5:
    total = preciopantalon*cantidad
elif cantidad >= 5 and cantidad < 12:
    preciopantalon -= (preciopantalon*0.12)
    total = cantidad*preciopantalon
else:
    preciopantalon -= (preciopantalon*0.3)
    total = cantidad*preciopantalon

print("El total es ", total)