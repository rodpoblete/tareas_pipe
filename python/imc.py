# IMC = (Peso / altura^2)
# IMC < 20 Bajo peso
# IMC >= 20 || IMC <= 25 Normal
# IMC > 25 Sobrepeso

peso_actual = int(input("Ingrese su peso (en kilos): "))
altura = float(input("Ingrese su altura (en metros): "))
IMC = peso_actual / altura ** 2

if IMC < 20:
    peso_ideal = 20 * altura ** 2
    subir_peso = peso_ideal - peso_actual
    print(f"Bajo Peso, debes subir {round(subir_peso, 4)} kilos para tu peso ideal.")

elif IMC >= 20 and IMC <= 25:
    print("Normal, estas dentro del rango normal de peso.")

else:
    peso_ideal = 25 * altura ** 2
    bajar_peso = peso_actual - peso_ideal
    print(f"Sobrepeso, debes bajar {round(bajar_peso, 4)} kilos para tu peso ideal.")

