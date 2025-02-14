Algoritmo Ejercicio_14_factura_luz_electrica
	//entradas
	Escribir "Indique la lectura de la factura del mes anterior"
	Leer lectura1
	Escribir "Indique el costo por kilovatio del mes anterior"
	Leer costo1
	Escribir "Indique la lectura de la factura actual"
	Leer lectura2
	Escribir "Indique el costo por kilovatio del mes actual"
	Leer costo2
	//caja negra
	promediolectura=((lectura1+lectura2)/2)
	promediocosto=((costo1+costo2)/2)
	montototal=(promediolectura*promediocosto)
	//salida
	Escribir "El monto total a pagar es de: ", montototal
FinAlgoritmo
