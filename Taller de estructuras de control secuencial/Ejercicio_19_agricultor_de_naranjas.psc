Algoritmo Ejercicio_19_agricultor_de_naranjas
	//entradas
	Escribir "Ingrese la cantidad de naranjas compradas (x)"
	Leer lote
	Escribir "Ingrese el valor de la docena de naranjas (y)"
	Leer docena
	Escribir "Ingrese el valor total de ventas (K)"
	Leer ganancia
	//caja negra
	Costototaldocenas= ((lote / 12)* docena)
	Valortotalganancia = (ganancia - Costototaldocenas)
	Pganancia = ((Valortotalganancia / Costototaldocenas)*100)
	//salidas
	Escribir "El porcentaje de ganancia es de: ", Pganancia "%"
FinAlgoritmo
