Algoritmo Comisiones_de_un_vendedor
	Escribir  "Digite las 3 ventas realizadas en el mes"
	Leer  venta1 , venta2, venta3
	Escribir "Digite su sueldo base"
	Leer  base
	Comi<-(venta1*0.10)+(venta2*0.10)+(venta3*0.10)
	Sueldo <- base + Comi
	Escribir  "La comisi�n recibida es:"  Comi
	Escribir  "Su sueldo total es:"  Sueldo
FinAlgoritmo
