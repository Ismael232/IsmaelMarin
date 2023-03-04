print("""
    -------MENU--------
    a. Area de un circulo
    b. Area de un triangulo
    c. Area de un cuadrado
"""
)
opcion = input("Seleccione una opcion: ")

if opcion == "a":
    radio = float(input("Escriba el radio: "))
    areaCirculo = 3.1415*radio**2
    print(f"El area del circulo es: {areaCirculo}")

elif opcion == "b":
        base = float(input("Indicar la base: "))
        altura = float(input("Indicar la altura: "))
        areaTriangulo = base*altura/2
        print(f"El area del triangulo es: {areaTriangulo}")
        
elif opcion == "c":
            lado = float(input("Escriba un lado: "))
            areaCuadrado = lado**2
            print(f"El area del cuadrado es: {areaCuadrado}")
else:
    print("Respuesta no valida")
