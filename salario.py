def calcular_salario(horas, pago_hora):
    salario = horas * pago_hora
    return salario

def main():
    horas = 40
    pago_hora = 5

    resultado = calcular_salario(horas, pago_hora)
    print("El salario semanal es:", resultado)

main()