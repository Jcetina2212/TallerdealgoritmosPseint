#entradas
inver=float(input("Digite el valor invertido:"))
m=int(input("Digite los meses trascurridos tras la inversión:"))
#caja negra
ganacia=(0.02*m)*inver#float
Total=ganacia+inver#float
#salidas
print(f"La ganacia obtenida luego de los meses trascurridos tras la inversión es de:{ganacia} y El total de dinero es:{Total}")
