#entradas
vent1=float(input("Digite el valor de la venta 1:"))
vent2=float(input("Digite el valor de la venta 2:"))
vent3=float(input("Digite el valor de la venta 3:"))
base=float(input("Digite su sueldo base:"))
#caja negra
comi=(vent1*0.10)+(vent2*0.10)+(vent3*0.10)
sueldo=base+comi
#salidas
print(f"La comisison por las 3 ventas es de:{comi} y el sueldo total es de:{sueldo}")
