Algoritmo Ejercicio_8_petrimetro_de_un_triangulo
	//entradas
	Escribir "Ingrese la medida del lado A"
	Leer A
	Escribir "Ingrese la medida del lado B"
	Leer B
	Escribir "Ingrese la medida del lado C"
	Leer C
	//caja negra
	// calcular el semíperimetro
	s=((A+B+C)/2)
	//calcular el área
	Area= raiz(s*(s-a)*(s-b)*(s-c))
	//salida
	Escribir "El Semíperimetro del triangulo es de: ", s
	Escribir "El Área del triangulo es de:  ", Area
FinAlgoritmo