#entradas
Ht=int(input("Digite la cantidad de horas trabajas:"))
Ph=float(input("Digete el precio al que le pagan la hora:"))
#caja negra
s_b=Ph*Ht
des=0.2*s_b#float
s_n=s_b-des#float
#salidas
print(f"EL descuento realizado por concepto de inpuesto es de:{des} y el salario neto es de:{s_n}")