#Entradas
import math as math
A=int(input("Ingrese la medida del lado A: "))
B=int(input("Ingrese la medida del lado B: "))
C=int(input("Ingrese la medida del lado C: "))
#Caja_negra
Semip=((A+B+C)/2)
Area=math.sqrt(Semip*(Semip-A)*(Semip-B)*(Semip-C))
#Salida
print("El Semíperimetro del triangulo es de: ", Semip)
print("El Área del triangulo es de :", Area)