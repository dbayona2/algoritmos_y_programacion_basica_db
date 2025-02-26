#Entrada
anterior=int(input("Ingrese la lectural anterior: "))
actual=int(input("Ingrese la lectural actual: "))
#Caja_negra ><
diferencia=(anterior-actual)
if (diferencia>=0 and diferencia<=100):
    print ("Monto a pagar por consumo de luz eléctrica y servicio de aseo urbano: ", (diferencia*4600), "COP")
elif (diferencia>=101 and diferencia<=300):
    print ("Monto a pagar por consumo de luz eléctrica y servicio de aseo urbano: ", (diferencia*80000), "COP")
elif (diferencia>=301 and diferencia<=500):
    print ("Monto a pagar por consumo de luz eléctrica y servicio de aseo urbano: ", (diferencia*100000), "COP")  
elif (diferencia>=501):
    print ("Monto a pagar por consumo de luz eléctrica y servicio de aseo urbano: ", (diferencia*120000), "COP")