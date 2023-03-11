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