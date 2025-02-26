#Entradas
inversion=int(input("Cantidad a invertir: "))
tasa=int(input("Tasa de interes: "))
#Caja_negra
interes=(inversion*tasa)/100
if (interes >= 100000):
    suma=(inversion+interes)
    print ("Dinero total en su cuenta es de: ", suma)
else:
    print ("El interes es inferior a 100000 COP")