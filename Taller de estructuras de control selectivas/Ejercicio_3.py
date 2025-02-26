#Entrada
a=int(input("Ingrese el dato A: "))
b=int(input("Ingrese el dato B: "))
c=int(input("Ingrese el dato C: "))
d=int(input("Ingrese el dato D: "))
#caja_negra
if (d==0):
    ec1=((a-c)**2)
    print("El resultado de la expresión es: ", ec1)
elif (d>0):
    ec2=((a-b)**3)/d
    print("El resultado de la expresión es: ",ec2)