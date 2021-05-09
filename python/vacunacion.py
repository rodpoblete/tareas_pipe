def principal():
    """Funcion que recibe por teclado datos de personas y muestra por pantalla totales de vacunación y porcentajes"""

    # Declaración de variables.
    personas_primera_dosis = 0
    promedio_edad_mujeres_vacunadas = 0
    porcentaje_mujeres_vacunadas = 0
    cantidad_vacunas_pfizer_aplicadas = 0

    # Captura por teclado de la cantidad de personas citadas.
    cantidad_personas_citadas = int(input("Ingrese cantidad de personas citadas: "))

    # Ciclo que itera sobre la cantidad de personas citadas para vacunación.
    for persona in range(cantidad_personas_citadas):
        edad = int(input(f"Ingrese edad de la persona n°{persona + 1}: "))
        genero = input(f"Ingrese genero (M o H) de la persona n°{persona + 1}: ")
        numero_vacuna = int(
            input(f"Ingrese numero de vacuna (1 o 2) de la persona n°{persona + 1}: ")
        )
        tipo_vacuna = input(
            f"Ingrese tipo de vacuna (P/S) de la persona n°{persona + 1}: "
        )

        # Condicionales para sumar a los acumuladores según rúbrica.
        if numero_vacuna == 1:
            personas_primera_dosis += 1

        if genero == "M":
            promedio_edad_mujeres_vacunadas += edad
            porcentaje_mujeres_vacunadas += 1

        if tipo_vacuna == "P":
            cantidad_vacunas_pfizer_aplicadas += 1

    # Impresión de valores solicitados por pantalla.
    print(
        f"La cantidad de personas vacunadas con primera dosis es: {personas_primera_dosis}"
    )
    print(
        f"El promedio de edad de las mujeres vacunadas es de: {int(promedio_edad_mujeres_vacunadas / cantidad_personas_citadas)} años"
    )
    print(
        f"El procentaje de mujeres vacunadas es de: {int((porcentaje_mujeres_vacunadas/ cantidad_personas_citadas) * 100)}%"
    )
    print(f"Cantidad de vacunas Pfizer aplicadas: {cantidad_vacunas_pfizer_aplicadas}")


if __name__ == "__main__":
    principal()
