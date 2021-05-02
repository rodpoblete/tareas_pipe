# Longitud comprendida 1,20 y 1,30 (aptas para el corte)

piezas = int(input("Ingrese la cantidad de piezas a procesar: "))
piezas_aptas = 0

for pieza in range(piezas):
    longitud_pieza = float(
        input(f"Ingrese longitud de perfil de la pieza n°{pieza + 1}: ")
    )

    if round(longitud_pieza, 2) >= 1.20 and round(longitud_pieza, 2) <= 1.30:
        piezas_aptas += 1

print(f"La cantidad de piezas aptas en el lote son: {piezas_aptas}")
