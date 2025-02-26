#Entradas
temperatura=float(input("Digite temperatura: "))
if(temperatura>85):
    print("Natacion")
elif(temperatura>=71 and temperatura<=85):
    print("Tenis")
elif(temperatura>=33 and temperatura<=70):
    print("Golf")
elif(temperatura>=11 and temperatura<=32):
    print("Esquí")
elif(temperatura<=10):
    print("Marcha")