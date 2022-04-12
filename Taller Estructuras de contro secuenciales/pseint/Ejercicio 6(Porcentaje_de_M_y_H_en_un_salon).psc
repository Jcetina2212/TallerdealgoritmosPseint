Algoritmo Porcentaje_de_M_y_H_en_un_salon
	Escribir "Ingrese la cantidad de Hombres"
	Leer H
	Escribir "Ingrese la cantidad de Mujeres"
	Leer M
	Total<-H+M
	porc_H<-redon((H*100)/Total)
	porc_M<-redon((M*100)/Total)
	Escribir "El porcentaje de Mujeres es:" porc_M
	Escribir "El porcentaje de Hombres es:" porc_H
FinAlgoritmo
