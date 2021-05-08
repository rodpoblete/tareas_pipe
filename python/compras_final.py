"""
Confeccionar un programa que solicite ingresar las compras de una persona que lleva n
productos distintos, para ello el cajero debe solicitar a la persona la cantidad de
productos que lleva, además del precio de cada producto y la cantidad que compra de
cada producto, se debe realizar la suma de la compra y mostrar el valor total a pagar
por el cliente. El cálculo de precio por la cantidad comprada lo debe realizar la función
precio_ cantidad, que realizará el cálculo y devolverá el resultado al programa principal
para que sume la compra. Nota: debe utilizar argumento y retorno de valor en la
función.
"""


def principal():
    """Función que captura la cantidad de productos a comprar e imprime por pantalla
    la suma de la compra total."""
    n_productos = int(input("Ingrese la cantidad de productos que desea llevar: "))
    suma_total_compra = precio_cantidad(n_productos)
    print(
        f"La suma total de la compra de {n_productos} producto(s) es de: {suma_total_compra}"
    )


def precio_cantidad(n_productos):
    """Función que calcula el precio por la cantidad indicada por el cliente."""
    suma_precios = 0
    for producto in range(n_productos):
        precio_por_producto = int(
            input(f"Ingrese el valor del producto n°{producto + 1}: ")
        )
        suma_precios += precio_por_producto
    return suma_precios


if __name__ == "__main__":
    principal()
