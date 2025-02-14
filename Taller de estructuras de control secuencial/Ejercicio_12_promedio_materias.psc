Algoritmo Ejercicio_12_promedio_materias
	//entradas
	Escribir "Escriba la nota del examen de matematicas"
	Leer notaexamenmatematicas
	Escribir "Escriba la nota de la tarea 1 de matematicas"
	Leer tarea1mate
	Escribir "Escriba la nota de la tarea 2 de matematicas"
	Leer tarea2mate
	Escribir "Escriba la nota de la tarea 3 de matematicas"
	Leer tarea3mate
	Escribir "Escriba la nota del examen de fisica"
	Leer notaexamenfisica
	Escribir "Escriba la nota de la tarea 1 de fisica"
	Leer tarea1fisica
	Escribir "Escriba la nota de la tarea 2 de fisica"
	Leer tarea2fisica
	Escribir "Escriba la nota del examen de quimica"
	Leer notaexamenquimica
	Escribir "Escriba la nota de la tarea 1 de quimica"
	Leer tarea1quimica
	Escribir "Escriba la nota de la tarea 2 de quimica"
	Leer tarea2quimica
	Escribir "Escriba la nota de la tarea 3 de quimica"
	Leer tarea3quimica
	//caja negra
	//promedio matematicas
	promediomate=redon((0.90*notaexamenmatematicas)+(0.10*((tarea1mate+tarea2mate+tarea3mate)/3)))
	//promedio fisica
	promediofisica=((0.80*notaexamenfisica)+(0.20*((tarea1fisica+tarea2fisica)/2)))
	//promedio quimica
	promedioquimica=((0.85*notaexamenquimica)+(0.15*((tarea1quimica+tarea2quimica+tarea3quimica)/3)))
	//promedio general
	promediogeneral=((promediomate+promediofisica+promedioquimica)/3)
	//salidas
	Escribir "El promedio general en las 3 materias es de: ", promediogeneral
	Escribir "El promedio en matematicas es de: ", promediomate
	Escribir "El promedio en fisica es de: ", promediofisica
	Escribir "El promedio en quimica es de: ", promedioquimica
FinAlgoritmo
