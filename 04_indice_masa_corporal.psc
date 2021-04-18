Algoritmo indice_masa_corporal
	// IMC = Peso / altura^2 (peso en kilos; altura en metros)
	// IMC < 20 bajo peso
	// IMC >= 20 y IMC <= 25 Normal
	// IMC > 25 Sobrepeso
	Definir peso_actual Como Entero
	Definir altura Como Real
	Escribir Sin Saltar"Ingrese su peso (en kilos): "
	Leer peso_actual
	Escribir Sin Saltar "Ingrese su altura (en mts): "
	Leer altura
	IMC = (peso_actual / altura^2)
	Si IMC < 20 Entonces
		peso_ideal = 20 * altura^2
		subir_peso = peso_ideal - peso_actual
		Escribir Sin Saltar "Estás bajo de peso, debes subir ", subir_peso, "kls."
	SiNo
		Si IMC >= 20 y IMC <= 25
			Escribir "Estas en el rango de peso normal"
		SiNo
			peso_ideal = 25 * altura^2
			bajar_peso = peso_actual - peso_ideal
			Escribir Sin Saltar "Estás con sobrepeso, debes bajar ", bajar_peso, "kls."
		FinSi
	Fin Si
FinAlgoritmo
