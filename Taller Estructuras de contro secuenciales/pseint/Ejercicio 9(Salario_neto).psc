Algoritmo Salario_neto
	Escribir "Digite la cantidad de horas trabajadas"
	Leer Ht
	Escribir "Digite el precio al que se le paga por hora"
	Leer Ph
	s_b<-Ph*Ht
	des<-0.2*s_b
	s_n<-s_b-des
	Escribir "El descuento por concepto de inpuesto es de:" des
	Escribir "El salarion neto es de:" s_n
FinAlgoritmo
