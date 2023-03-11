#def dibujoCuadrado():
#    lado = int(input("Ingrese el lado del cuadrado: "))
#    for i in range(lado):
#        print("#  "*lado)
#
#def identificador2():
lista = []
numPares = []
cantidad = int(input("Indique la cantidad de numeros: "))
for i in range(cantidad):
    auxiliar = int(input(f"Indique el elemento{i+1}: "))
    lista.append(auxiliar)

for i in lista:
    if i % 2 == 0:
        numPares.append(i)
print(numPares)