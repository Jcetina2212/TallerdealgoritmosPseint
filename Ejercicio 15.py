#entradas
pfp=float(input("Digite el presio final pagado:"))
pvp=float(input("Digite el presio de venta al publico:"))
#caja negra
Descuento=pvp-pfp
Porcentaje=(Descuento/pvp)*100
#salidas
print(f"El Descuento obtenido por el producto es de:{Porcentaje} %")
