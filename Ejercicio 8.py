import math
#Entradas
a=float(input("Ingese lado a:"))
b=float(input("Ingrese lado b:"))
c=float(input("Ingrese lado c:"))
#caja negra
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
#salidas
print("El área es:",round(area,2))