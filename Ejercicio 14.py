#entradas
L_an=float(input("Lectura anterior"))
L_ac=float(input("Lectura actual"))
Kl=float(input("Costo por kilovatio"))
#caja negra
Pago_actual=Kl*L_ac
Pago_anterior=Kl*L_an
Promedio=(Pago_actual+Pago_anterior)/2
#salidas
print(f"El costo a pagar por un mes es de:{Promedio}")