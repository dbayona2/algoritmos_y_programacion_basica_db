#Entradas
sueldo_base=int(input("Ingrese su sueldo base: "))
#Caja_negra
comisiones=(sueldo_base*10)/100
sueldo_y_comisiones=(sueldo_base+comisiones)
#Salida
print("Las comisiones del mes son: ", comisiones)
print("El total del sueldo del mes es de: ", sueldo_y_comisiones)