Algoritmo Ejercicio_21_recargo_por_pago_a_cuotas
	//entradas
	Escribir "Indique precio de contando"
	Leer pcontado
	Escribir "Indique precio de pago a crédito"
	Leer pcredito
	//caja negra
	valorcuota = (pcredito /12)
	valorrecargo = (pcredito - pcontado)
	Precarga = (valorrecargo * pcontado ) /100
	//salida
	Escribir "El valor de cuota por 12 meses es de " , valorcuota " COP"
	Escribir "El porcentaje de recargo es del: ", Precarga "%"
FinAlgoritmo
