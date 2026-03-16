def calcular_promedio(nota1, nota2):
    promedio = (nota1 + nota2) / 2
    return promedio

def main():
    nota1 = 8
    nota2 = 9

    resultado = calcular_promedio(nota1, nota2)
    print("El promedio es:", resultado)

main()