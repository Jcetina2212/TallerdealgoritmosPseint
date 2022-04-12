#entradas
Precio=int(input("Digitel presio del producto:"))
#caja negra
Des=0.15*Precio#float
Tol=Precio-Des#float
#salidas
print(f"El descuento es de:{Des} y el total a pgar con un descuento del 15 porciento es:{Tol}")