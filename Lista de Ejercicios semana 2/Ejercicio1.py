def dibujoCuadrado():
    lado = int(input("Ingrese el lado del cuadrado: "))
    for i in range(lado):
        print("#  "*lado)

def identificadorDePares():
 lista = []
 numPares = []
 cantidad = int(input("Indique la cantidad de numeros: "))
 for i in range(cantidad):
     auxiliar = int(input(f"Indique el numero {i+1}: "))
     lista.append(auxiliar)
 
 for i in lista:
     if i % 2 == 0:
         numPares.append(i)
 print(f"Los numeros pare son: {numPares}")

def personasMayores():
 elementos = int(input("Ingrese la cantidad de elementos: "))
 personas = []
 for i in range(elementos):
     nombre = input(f"Ingrese el nombre {i+1}: ")
     edad = int(input(f"Ingrese la edad {i+1}: "))
     personas.append([nombre,edad])
 
 personasMayores = []
 
 for index,elementos in enumerate(personas):
     if elementos[1] >= 18:
         personasMayores.append(elementos)
 
 print(personasMayores)

 ## MENU DE LA FUNCION PRINCIPAL

print(""" *******MENU********
        1.
        2.
        3.""")
opcion = input("Elija una opcion: ")
if opcion == "1":
   dibujoCuadrado()
elif opcion == "2":
   identificadorDePares()
elif opcion == "3":
   personasMayores()
else:
    print("Elija una opcion valida :/")