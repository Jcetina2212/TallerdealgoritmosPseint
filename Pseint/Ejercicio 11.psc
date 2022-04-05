Algoritmo Notas_de_Algoritmos
	Escribir "Notas de los parciales"
	Leer n1
	Leer n2
	Leer n3
	Prom<-(n1+n2+n3)/3
	Nparc<-0.55*Prom
	Escribir "Nota examen final"
	Leer e1
	E1<-0.30*e1
	Escribir "Notas trabajo final"
	Leer t1
	T1<-0.15*t1
	Notas<-redon(Nparc+e1+t1)
	Escribir "La nota de Algoritmos es:" Notas
FinAlgoritmo
