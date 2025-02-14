Algoritmo Ejercicio_11_asignaciones_deducciones_y_sueldo_neto
	//entradas
	Escribir "Nombre"
	Leer nombre
	Escribir "Salario base"
	Leer salariobase
	Escribir "Cantidad de hijos"
	Leer hijos
	Escribir "Cantidad de dias trabajados"
	Leer diastrabajados
	Escribir "Cantidad de horas trabajadas"
	Leer horasnormales
	Escribir "Cantidad de horas extras trabajadas"
	Leer horasextras
	//caja negra
	//Asignaciones
	Valorporhoranormal=trunc((salariobase/24)/8)
	Valortotalhoranormal=trunc(Valorporhoranormal*horasnormales)
	Valorporhoraextra=(Valorporhoranormal/0.75)
	Valortotalhoraextra=(Valorporhoraextra*horasextras)
	ingresoactualizaciona=(250000)
	ingresoporhijo=(173000*hijos)
	ingresoprimahogar=(180000)
	//Deducciones
	Pagoforzoso=((salariobase*5)/100)
	politicahabitacional=((salariobase*2)/100)
	cajadeahorro=((salariobase*7)/100)
	//salario neto
	salarioneto=((Valorporhoranormal*horasnormales)+(Valorporhoraextra*horasextras)+(ingresoactualizaciona)+(ingresoporhijo)+(ingresoprimahogar)-(Pagoforzoso)-(politicahabitacional)-(cajadeahorro))
	//salidas Asignaciones
	Escribir "COMPROBANTE DE PAGO"
	Escribir "Nombre: ", nombre
	Escribir "Fecha de pago: 30/12/2024"
	Escribir "Dias laborados en el mes ", diastrabajados
	Escribir "Valor por hora normal: ", Valorporhoranormal, " por ", horasnormales, " horas trabajadas en el mes, para un total de: ",Valortotalhoranormal
	Escribir "Valor por hora extra: ", Valorporhoraextra, " por ", horasextras, " horas extras trabajadas en el mes, para un total de: ", Valortotalhoraextra
	Escribir "Ingreso por actualizacion academica: ", ingresoactualizaciona
	Escribir "Ingreso por hijos: ", ingresoporhijo
	Escribir "Ingreso por prima hogar: ", ingresoprimahogar
	//salidas Deducciones
	Escribir "Deduccion por Pago forzoso 2%: ", Pagoforzoso
	Escribir "Deduccion por Politica Habitacional 5%: ", politicahabitacional
	Escribir "Deduccion por Caja de ahorro 7%: ", cajadeahorro
	//salida salario neto
	Escribir "Valor neto a pagar: ", salarioneto
FinAlgoritmo
