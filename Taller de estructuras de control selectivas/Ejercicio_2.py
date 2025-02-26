#Entrada
sueldo=int(input("Ingrese su salario bruto: "))
#Caja_negra
if (sueldo<=900000):
    print(sueldo/0.85)
else:
    print(sueldo/0.88)