Algoritmo  Area_de_un_triangulo
	Escribir "Ingrese el lado a"
	Leer a
	Escribir "Ingrese el lado b"
	Leer b
	Escribir "Ingrese el lado c"
	Leer c
	s<-(a+b+c)/2
	are<-redon(raiz(s*(s-a)*(s-b)*(s-c)))
	Escribir "El area es:" area 
FinAlgoritmo
