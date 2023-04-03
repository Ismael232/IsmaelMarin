from CapaLogica import *


while True:
    print ("""
            MENU DE OPERACIONES
            1)Añadir columna total de precio
            2)Leer datos de un excel y llevarlo a la base de datos
            3)Crear una tabla a la base de datos y agregar datos
            4)Salir """)
    
    option = int(input("Elija una opcion : "))
    valor = opcion(option)
    if valor == False:
        break