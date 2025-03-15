Algoritmo Ejercicio_7
	Definir num, contar Como Entero
	Escribir "Digite un número: "
	Leer num
	contador<-0
	
	Para contar<-1 Hasta num Hacer
		si num % contar = 0 Entonces
			contador<-contador+1
		FinSi
		
	FinPara
	si contador = 2 Entonces
		Escribir "Es primo"
	SiNo
		Escribir "No es primo"
	FinSi
FinAlgoritmo
