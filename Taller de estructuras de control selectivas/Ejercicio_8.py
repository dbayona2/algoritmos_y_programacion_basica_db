#Entradas
p=int(input("Ingrese el valor de P: "))
q=int(input("Ingrese el valor de Q: "))
#Caja_negra
if (((p**3)+(q**4)-(2*(p**2)))>680):
    print("P y Q satisfacen la expresión.")
else:
    print("P y Q no Satisfacen la expresión.")