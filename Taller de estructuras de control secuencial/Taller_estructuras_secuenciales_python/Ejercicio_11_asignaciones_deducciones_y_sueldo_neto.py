#Entradas
nombre=(input("Nombre: "))
salariobase=int(input("Ingrese su salario base: "))
hijos= int (input("Cantidad de hijos: "))
diastrabajados=int(input("Cantidad de dias trabajados: "))
horasnormales=int(input("Cantidad de horas trabajadas: "))
horasextras= int(input("Cantidad de horas extras trabajadas: "))
#Caja_negra_Asignaciones
Valorporhoranormal=round((salariobase/24)/8)
Valortotalhoranormal=round(Valorporhoranormal*horasnormales)
Valorporhoraextra=round(Valorporhoranormal/0.75)
Valortotalhoraextra=(Valorporhoraextra*horasextras)
ingresoactualizaciona=(250000)
ingresoporhijo=(173000*hijos)
ingresoprimahogar=(180000)
#Deducciones
Pagoforzoso=((salariobase*5)/100)
politicahabitacional=((salariobase*2)/100)
cajadeahorro=((salariobase*7)/100)
#Salario_neto
salarioneto=round((Valorporhoranormal*horasnormales)+(Valorporhoraextra*horasextras)+(ingresoactualizaciona)+(ingresoporhijo)+(ingresoprimahogar)-(Pagoforzoso)-(politicahabitacional)-(cajadeahorro))
#Salidas_Asignaciones
print("COMPROBANTE DE PAGO")
print("Nombre: ", nombre)
print("Fecha de pago: 30/12/2024")
print("Dias laborados en el mes ", diastrabajados)
print("Valor por hora normal: ", Valorporhoranormal, " por ", horasnormales, " horas trabajadas en el mes, para un total de: ",Valortotalhoranormal)
print("Valor por hora extra: ", Valorporhoraextra, " por ", horasextras, " horas extras trabajadas en el mes, para un total de: ", Valortotalhoraextra)
print("Ingreso por actualizacion academica: ", ingresoactualizaciona)
print("Ingreso por hijos: ", ingresoporhijo)
print("Ingreso por prima hogar: ", ingresoprimahogar)
#Salidas_Deducciones
print("Deduccion por Pago forzoso 2%: ", Pagoforzoso)
print("Deduccion por Politica Habitacional 5%: ", politicahabitacional)
print("Deduccion por Caja de ahorro 7%: ", cajadeahorro)
#Salida_salario_neto
print("Valor neto a pagar: ", salarioneto)