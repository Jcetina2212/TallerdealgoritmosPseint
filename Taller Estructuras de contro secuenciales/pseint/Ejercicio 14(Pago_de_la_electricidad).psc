Algoritmo Pago_de_la_electricidad
	Escribir "lectura anterior"
	Leer L_an
	Escribir "Lectura actual"
	Leer L_ac
	Escribir "Costo por kilovatio"
	Leer Kl
	Pago_actual<-Kl*L_ac
	Pago_anteriorerior<-Kl*L_an
	Diferencia<-Pago_actual-Pago_anterior
	Escribir"El costo actual es de:" Pago_actual
	Escribir "La Diferenciacon respecto al pago anterior es de:" Diferencia
FinAlgoritmo
