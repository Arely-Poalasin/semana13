# Declaración del método
def calcularTotal(precio, cantidad):
    total = precio * cantidad
    return total


# Función principal (main)
def main():
    precio = 10
    cantidad = 3

    resultado = calcularTotal(precio, cantidad)

    print("El total de la compra es:", resultado)


# Llamada al main
main()