Algoritmo mayoresMenoresEdad
	Definir edad, adulto_mayor, menores_edad Como Entero
	Para cantidad_personas<-1 Hasta 3 Con Paso cantidad_personas + 1 Hacer
		Escribir "Ingrese su edad: ",  "Persona N°", cantidad_personas
		Leer edad
		Si edad >= 65 Entonces
			adulto_mayor = adulto_mayor + 1
		SiNo						
			Si edad < 18 Entonces
				menores_edad = menores_edad + 1
			Fin Si
		Fin Si
	Fin Para
	Escribir "La cantidad de adultos mayores es: ", adulto_mayor
	Escribir "La cantidad de menores de edad es: ", menores_edad
FinAlgoritmo
