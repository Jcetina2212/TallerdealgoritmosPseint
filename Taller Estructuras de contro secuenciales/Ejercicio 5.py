P1=float(input("Digite nota del primer parcial:"))
P2=float(input("Digite nota del segundo parcial:"))
P3=float(input("Digite nota del tercer parcial:"))
Ex=float(input("Digite nota del examen final:"))
Tf=float(input("Digite notal del taller final:"))
#caja negra
Prom_P=(P1+P2+P3)/3
N_P=(0.55*Prom_P)
N_Ex=(0.30*Ex)
N_Tf=(0.15*Tf)
Calificacion=(N_P+N_Ex+N_Tf)
#salidas
print(f"La nota final de computacion es de:{round(Calificacion)}")
