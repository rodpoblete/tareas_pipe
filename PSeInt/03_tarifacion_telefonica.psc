Algoritmo tarifacion_telefonica
	// (duracion_llamada < 3 minutos) costo base $100 (ambos horarios)
	// horario diurno = (duracion_llamada > 3 minutos) $30 por minuto adicional
	// horario nocturno = (duracion_lammada > 3 minutos) $15 por minuto adicional
	// Horario Nocturno = 21:00 hasta 24:00
	
	Definir costo Como Entero
	Definir HORA_INICIO, HORA_TERMINO Como Real
	Escribir Sin Saltar "Ingrese Hora de inicio llamada (HH): "
	Leer hh_inicio
	Escribir Sin Saltar "Ingrese Minutos inicio de llamada (MM): "
	Leer mm_inicio 
	Escribir Sin Saltar "Ingrese hora término llamada (HH): "
	Leer hh_termino
	Escribir Sin Saltar "Ingrese minutos término llamada (MM): "
	Leer mm_termino
	// Calculamos a decimal
	HORA_INICIO = hh_inicio + mm_inicio / 60
	HORA_TERMINO = hh_termino + mm_termino / 60
	horas_diferencia = HORA_TERMINO - HORA_INICIO
	duracion_en_minutos = horas_diferencia * 60
	
	Si (hh_inicio >= 21) Y (hh_termino <= 24) Entonces
		// Horario Nocturno
		Si duracion_en_minutos < 3 Entonces
			costo = 100
			Escribir "Su llamada fue de ", duracion_en_minutos, " min."
			Escribir "Fue realizada en horario NOCTURNO"
			Escribir "El costo fue de ", costo
		SiNo
			costo = 100 + trunc(duracion_en_minutos - 3) * 15
			Escribir "Su llamada fue de ", duracion_en_minutos, " min."
			Escribir "Fue realizada en horario NOCTURNO"
			Escribir "El costo fue de ", costo
		Fin Si
	SiNo
		// Horario Diurno
		Si duracion_en_minutos < 3 Entonces
			costo = 100
			Escribir "Su llamada fue de ", duracion_en_minutos, " min."
			Escribir "Fue realizada en horario DIURNO"
			Escribir "El costo fue de ", costo
		SiNo
			costo = 100 + trunc(duracion_en_minutos - 3) * 30
			Escribir "Su llamada fue de ", duracion_en_minutos, " min."
			Escribir "Fue realizada en horario DIURNO"
			Escribir "El costo fue de ", costo
		Fin Si
	Fin Si
FinAlgoritmo
