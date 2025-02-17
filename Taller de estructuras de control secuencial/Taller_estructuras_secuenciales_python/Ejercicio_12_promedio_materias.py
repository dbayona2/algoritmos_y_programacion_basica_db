#Entradas
notaexamenmatematicas= int(input("Escriba la nota del examen de matematicas: "))
tarea1mate=	int(input ("Escriba la nota de la tarea 1 de matematicas: "))
tarea2mate= int(input("Escriba la nota de la tarea 2 de matematicas: "))
tarea3mate= int(input("Escriba la nota de la tarea 3 de matematicas: "))
notaexamenfisica= int(input("Escriba la nota del examen de fisica: "))
tarea1fisica= int(input("Escriba la nota de la tarea 1 de fisica: "))
tarea2fisica= int(input("Escriba la nota de la tarea 2 de fisica: "))
notaexamenquimica= int(input("Escriba la nota del examen de quimica: "))
tarea1quimica= int(input("Escriba la nota de la tarea 1 de quimica: "))
tarea2quimica= int(input("Escriba la nota de la tarea 2 de quimica: "))
tarea3quimica= int(input("Escriba la nota de la tarea 3 de quimica: "))
#Caja_negra
#Promedio_matematicas
promediomate=round((0.90*notaexamenmatematicas)+(0.10*((tarea1mate+tarea2mate+tarea3mate)/3)))
#Promedio_fisica
promediofisica=round((0.80*notaexamenfisica)+(0.20*((tarea1fisica+tarea2fisica)/2)))
#Promedio_quimica
promedioquimica=round((0.85*notaexamenquimica)+(0.15*((tarea1quimica+tarea2quimica+tarea3quimica)/3)))
#Promedio_general
promediogeneral=round((promediomate+promediofisica+promedioquimica)/3)
#Salidas
print("El promedio general en las 3 materias es de: ", promediogeneral)
print("El promedio en matematicas es de: ", promediomate)
print("El promedio en fisica es de: ", promediofisica)
print("El promedio en quimica es de: ", promedioquimica)