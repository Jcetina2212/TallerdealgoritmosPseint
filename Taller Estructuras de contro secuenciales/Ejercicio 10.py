#entada_1
Ch_AS=float(input("Digite la cantidad en chelines austriacos:"))
#caja negra_1
pesetas=Ch_AS*(956.871/100)
#salida_1
print(f"Su equivalencia en pesetas es de:{round(pesetas,5)}")
#entrada_2
Dc_Gr=float(input("Digite la cantidad en dracmas griegos:"))
#caja negra_2
Fr_fr=Dc_Gr*(88.607/100)*(1/20.110)
#salidas_2
print(f"La cantidad en francos franceses es de:{round(Fr_fr,5)}")
#entrada_3
Pes=float(input("Digite la cantidad en pesetas:"))
#caja negra_3
Dolares=Pes/122.499
Libras_italianas=Pes*(100/9.289)
#salidas_3
print(f"La cantidad en Dolares es de:{round(Dolares,5)} y la cantidad en libras Libras_italianas es de:{round(Libras_italianas,5)} ")