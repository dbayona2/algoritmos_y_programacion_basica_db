#Entradas
smensual=int(input("Ingrese su salario base mensual: "))
horas=int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
#Caja_negra
salariobasexdia= (smensual/30)
salariobasexhora = (salariobasexdia/8)
salarionetoxdia = (salariobasexdia*0.8)
salarionetoxhora = (salarionetoxdia/8)
salarioneto = (salarionetoxhora*horas)
salarioneto1 = round(salarioneto)
#Salidas
print("Salario NETO: ", salarioneto1 , "por", horas, "trabajadas en el mes")