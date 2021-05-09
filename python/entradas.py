def principal():
    """Funcion que captura la cantidad de entradas y muestra por pantalla precio y cantidad según tipo."""

    # Declaración de variables
    cantidad_vendidas_general = 0
    cantidad_vendidas_socios = 0
    cantidad_vendidas_total = 0

    # Ciclo que itera hasta que el usuario indique la interrupción.
    while True:

        # Captura por teclado de los datos de las entradas.
        cantidad_entradas = int(input("Ingrese cantidad de entradas a vender: "))
        tipo_entrada = int(
            input("Ingrese tipo de entrada a vender (1: Socio o 2: General): ")
        )

        # Condicionales para incrementar los acumuladores según rúbrica.
        if tipo_entrada == 1:
            cantidad_vendidas_socios += cantidad_entradas
        elif tipo_entrada == 2:
            cantidad_vendidas_general += cantidad_entradas

        # Se llama a la función calculo_entradas y se captura el valor de retorno en la variable total_pagar.
        total_pagar = calculo_entradas(cantidad_entradas, tipo_entrada)
        print(f"El precio de la venta es de: ${total_pagar}")

        # Se pregunta al usuario por teclado que indique si quiere interrumpir el ciclo y se captura en la
        # variable opcion.
        opcion = input("Desea seguir vendiendo entradas (si/no): ")

        # Condicional para indicar que el ciclo continúe o se detenga y se salga del bloque de ejecución.
        if opcion == "no":
            print(
                f"La cantidad de entradas totales vendidas fue de: {cantidad_vendidas_general + cantidad_vendidas_socios}"
            )
            print(
                f"La cantidad de entradas vendidas generales fueron: {cantidad_vendidas_general}"
            )
            print(
                f"La cantidad de entradas vendidas socios fueron: {cantidad_vendidas_socios}"
            )
            break
        elif opcion == "si":
            continue


def calculo_entradas(cantidad_entradas, tipo_entrada):
    """Función que recibe cantidad de entradas, tipo y calcula su valor dependiendo del tipo."""

    # Se establecen los valores de las entradas.
    precio_entrada_general = 8500
    precio_entrada_socios = int(
        precio_entrada_general - ((20 * precio_entrada_general) / 100)
    )

    # Ciclo de condiciones que incrementa calcula el total del valor y lo retorna.
    if tipo_entrada == 2:
        total_entradas_general = precio_entrada_general * cantidad_entradas
        return total_entradas_general
    elif tipo_entrada == 1:
        total_entradas_socios = precio_entrada_socios * cantidad_entradas
        return total_entradas_socios


if __name__ == "__main__":
    principal()
