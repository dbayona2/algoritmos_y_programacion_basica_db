#Entradas
metros=int(input("Cantidad de metros: "))
#Caja_negra
Pulgadas=(metros*39.27)
Pulgadasr=round(Pulgadas, 2)
Pies=(Pulgadas/12)
Piesr=round(Pies, 2)
#Salidas
print("Cantidad de metros: ", metros)
print("Cantidad de pulgadas: ", Pulgadasr)
print("Cantidad de pies: ", Piesr)