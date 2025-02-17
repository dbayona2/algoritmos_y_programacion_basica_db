#Entradas
parcial=int(input("Escriba la nota de sus calificaciones parciales: "))
examen=int(input("Escriba la nota de su examen final: "))
trabajo=int(input("Escriba la nota de su trabajo final: "))
#Caja_negra
promedio=((0.55*parcial)+(0.30*examen)+(0.15*trabajo))
#Salida
print("Su Calificación final es de: ",promedio)