#Entradas
kilometros=int(input("Ingrese la cantidad de kilometros recorridos: "))
#Caja_negra
if (kilometros<300):
    print("Valor a cancelar 50000 COP")
elif (kilometros>300 and kilometros<=1000):
    ec1=((kilometros-300)*30000)
    print("Valor a cancelar ", (70000+ec1), "COP")
elif (kilometros>1000):
    ec2=((kilometros-1000)*9000)
    print("Valor a cancelar ", (150000+ec2), "COP")