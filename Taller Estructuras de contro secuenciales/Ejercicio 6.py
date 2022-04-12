#entradas
H=int(input("Ingrese la cantidad de hombres:"))
M=int(input("Ingrese la cantidad de mujeres:"))
Total=M+H
porH=(H*100)/Total
porM=(M*100)/Total
print(f"El porcentaje de Mujeres es:{round(porM)} y el porcntaje de Hombres es:{round(porH)}")