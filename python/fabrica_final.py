"""Una planta que fabrica perfiles de hierro posee un lote de n piezas. Confeccionar un
programa que pida ingresar por teclado la cantidad de piezas a procesar y luego ingrese
la longitud de cada perfil; sabiendo que la pieza cuya longitud esté comprendida en el
rango de 1,20 y 1,30 son aptas. La longitud envíela a una función para que responda si
es apta o no, el programa principal debe contar y mostrar la cantidad de piezas aptas.
Nota: debe utilizar argumento y retorno de valor en la función."""

# Longitud comprendida 1,20 y 1,30 (aptas para el corte)


def principal():

    piezas = int(input("Ingrese la cantidad de piezas a procesar: "))
    piezas_aptas = False
    cantidad_piezas_aptas = 0

    for pieza in range(piezas):
        longitud_pieza = float(
            input(f"Ingrese longitud de perfil de la pieza n°{pieza + 1}: ")
        )
        piezas_aptas = evalua_piezas_aptas(longitud_pieza)
        if piezas_aptas == True:
            cantidad_piezas_aptas += 1
    print(f"La cantidad de piezas aptas es: {cantidad_piezas_aptas}")


def evalua_piezas_aptas(longitud_pieza):
    if round(longitud_pieza, 2) >= 1.20 and round(longitud_pieza, 2) <= 1.30:
        return True
    else:
        return False


if __name__ == "__main__":
    principal()
