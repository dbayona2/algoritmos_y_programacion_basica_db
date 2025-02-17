#Entradas
hombres=int(input("Cantidad de hombres del grupo: "))
mujeres=int(input("Cantidad de mujeres del grupo: "))
#Caja_negra
Totalhym=(hombres+mujeres)
Pdehombres=(hombres/Totalhym)*100
PdemujereS=(mujeres/Totalhym)*100
#Salida
print("Total de personas: ", Totalhym)
print("Total de hombres del grupo: ", Pdehombres, "%")
print("Total de mujeres del grupo: ", PdemujereS, "%")