#Entradas
a=int(input("Ingrese el valor de A: "))
b=int(input("Ingrese el valor de B: "))
c=int(input("Ingrese el valor de C: "))
import math as math
#Caja_negra
d=(((b**2)-(4*a))*c)
if (d==0):
    ec1=(-b/(2*a))
    print (ec1)
elif (d>0):
    ec2=(-b+math.sqrt(b**2)-4*a*c)//(2*a)
    print(ec2)
    ec3=(-b-math.sqrt(b**2)-4*a*c)//(2*a)
    print (ec3)
elif (d<0):
    print("No tiene solución en los Reales")