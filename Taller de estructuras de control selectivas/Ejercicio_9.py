#Entradas
nombre=str(input("Ingrese su nombre: "))
montocompra=int(input("Ingrese el monto de su compra: "))
#Caja_negra
if (montocompra<50000):
    descuento=0
    print(nombre)
    print("Monto de la compra: ", montocompra, "COP")
    print("Monto a pagar: ", montocompra, "COP")
    print("Descuento recibido: ", descuento, "%")
elif (montocompra>=50000 and montocompra<100000):
    descuento= 5
    print(nombre)
    print("Monto de la compra: ",montocompra, "COP")
    print("Monto a pagar: ", (round(montocompra*0.95)), "COP")
    print("Descuento recibido: ", descuento, "%")
elif (montocompra>=100000 and montocompra<1500000):
    descuento= 18
    print(nombre)
    print("Monto de la compra: ",montocompra, "COP")
    print("Monto a pagar: ", (round(montocompra*0.82)), "COP")
    print("Descuento recibido: ", descuento, "%")
else:
    descuento= 25
    print(nombre)
    print("Monto de la compra: ",montocompra, "COP")
    print("Monto a pagar: ", (round(montocompra*0.75)), "COP")
    print("Descuento recibido: ", descuento, "%")