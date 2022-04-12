#entradas
from xml.sax.saxutils import prepare_input_source


gal=float(input("Ingrese la cantidad de galones consumidos "))
#caja negra
lit_c=gal*3.785
presio=lit_c*50000
#salidas
print(f"El valor a pagar es de:{presio}")
