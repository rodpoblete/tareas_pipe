Algoritmo filas
	Definir estatura, cantidad_personas Como Entero
	personas = "SI"  // inicialización de variable
	// No sabemos la cantidad (Mientras / Repetir)
	// Si sabemos la cantidad (para)
	Mientras personas == "SI" Hacer
		Escribir "Hay personas en la fila (SI/NO): "
		Leer personas_fila
		
		Si personas_fila == "SI" Entonces
			Escribir "Ingrese Estatura (en cm) :"
			Leer estatura
			Si estatura > 180 Entonces
				personas_altas = personas_altas + 1
			SiNo
				personas_bajas = personas_bajas + 1
			FinSi
		SiNo
			Si personas_fila == "NO" Entonces
				personas = "NO"
			FinSi
		FinSi
	Fin Mientras
	Escribir "La cantidad de personas altas son ", personas_altas
	Escribir "La cantidad de personas bajas son ", personas_bajas
FinAlgoritmo
