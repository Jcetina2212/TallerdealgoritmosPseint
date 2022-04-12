Algoritmo Notas_de_computación
	Escribir "Notas de los parciales"
	Leer P1,P2,P3
	Escribir "Nota del examen final"
	Leer Ex
	Escribir "Notal del trabajo final"
	Leer Tf
	Prom_P<-(P1+P2+P3)/3
	N_P<-(0.55*Prom_P)
	N_Ex<-(0.30*Ex)
	N_Tf<-(0.15*Tf)
	Calificacion<-redon((N_P+N_Ex+N_Tf))
	Escribir "La nota final del computacón es de:" Calificacion
FinAlgoritmo
