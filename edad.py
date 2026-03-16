def verificar_edad(edad, limite):
    if edad >= limite:
        return True
    else:
        return False

def main():
    edad = 20
    limite = 18

    resultado = verificar_edad(edad, limite)

    if resultado:
        print("La persona es mayor de edad")
    else:
        print("La persona es menor de edad")

main()