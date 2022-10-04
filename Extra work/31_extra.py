#31.-Un productor de leche lleva el registro de lo que produce en litros, 
#pero cuando entrega le pagan en galones. 1 galón = 3.785 litros, 
#cree un programa que le permita calcular cuanto ganará a partir de la 
#cantidad de galones producidos y el precio del litro.

#S.- Galones producidos:

#E.- 4

#S.- Precio del litro:

#E.- $25

#S.- Ganancia: $ 378.5

precio_galon = 3.785
litro = 0
galones_producidos = 0
pago = 0

print("Galones producidos: ",end="")
galones_producidos = int(input())

print("\nPrecio del litro: ", end="")
litro = int(input())

pago = (galones_producidos*precio_galon) * litro

print("\nLa ganancia es: ",pago)
