#Entradas
categoria=int(input("Indique su categoría: "))
sueldob=int(input("Indique su sueldo bruto: "))
#Caja_negra
if(sueldob<=900000 or sueldob<2000000) and (categoria==5):
    print ("Categoria 5")
    print ("Su nuevo sueldo bruto es de: ", (sueldob+(sueldob*60)/100))
elif(sueldob>=2000000 or sueldob<3600000) and (categoria==4):
    print ("Categoria 4")
    print ("Su nuevo sueldo bruto es de: ", (sueldob+(sueldob*40)/100))
elif(sueldob>=3600000 or sueldob<4300000) and (categoria==3):
    print ("Categoria 3")
    print ("Su nuevo sueldo bruto es de: ", (sueldob+(sueldob*20)/100))
elif(sueldob>=4300000 or sueldob<5000000) and (categoria==2):
    print ("Categoria 2")
    print ("Su nuevo sueldo bruto es de: ", (sueldob+(sueldob*15)/100))
elif(sueldob>=5000000) and (categoria==1):
    print ("Categoria 1")
    print ("Su nuevo sueldo bruto es de: ", (sueldob+(sueldob*10)/100))