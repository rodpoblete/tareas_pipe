Algoritmo numero_magico
	Definir numero_azar, intentos, numero_usuario Como Entero
	numero_azar = azar(100)
	Escribir numero_azar
	Repetir
		Escribir "Intenta adivinar el número (1-100):"
		Leer numero_usuario
		Si (numero_usuario > numero_azar) Entonces
			Escribir "MUY ALTO, sigue intentado"
		Fin Si
		Si (numero_usuario < numero_azar) y (numero_usuario <> numero_azar) Entonces
			Escribir "MUY BAJO, sigue intentando"
		FinSi
		Si (numero_usuario == numero_azar) Entonces
			Escribir "Felicidades haz adivinado el número"
		FinSi
		intentos = intentos + 1
	Hasta Que (numero_usuario == numero_azar)
	Escribir "Lo conseguiste en ", intentos, " intentos"
FinAlgoritmo
