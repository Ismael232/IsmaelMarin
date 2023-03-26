from Ejercicio2 import sorteo
import os
from datetime import datetime

########################   EJERCICIO 2  ########################################
"""
sort = sorteo(100,6)
sort.sorteoNumeros()
print(sort.lista)
"""
from Ejercicio3 import *

########################   EJERCICIO 3  ########################################
'''
def borrarPantalla():
    os.system('cls' if os.name=='nt' else 'clear')

menu = """
        --------MENU-----------
        1)Sunat
        2)Pokemon
        3)Salir
        """
menuSunat = """
        --------SUNAT-----------
        1)Ver tipo de cambio
        2)Comprar
        3)Vender
        4)Atras
        5)Salir
"""
menuPokemon = """
        --------POKEMON-----------
        1)Listar pokemon
        2)Buscar pokemon
        3)Atras
        4)Salir
"""
while True:
    print(menu)
    opcion = int(input("Selecione una opcion: "))
    if opcion == 1:
        borrarPantalla()
        print(menuSunat)
        opcion = int(input("Selecione una opcion: "))
        if opcion == 1:
            data = sunat()
            compra = data["compra"]
            venta = data["venta"]
            print(f"La compra esta: {compra}")
            print(f"La venta esta: {venta}")
            input("Presione una tecla para volver al menu... ")
            borrarPantalla()
        if opcion == 2:
            uno = casaCambio()
            cantidad = float(input("Ingrese la cantidad de dolar que desea comprar: "))
            soles = uno.compra(cantidad)
            print(f"La cantidad de soles a pagar es: {soles} ")
            input("Presione una tecla para volver al menu... ")
            borrarPantalla()
            continue
        if opcion == 3:
            uno = casaCambio()
            cantidad = float(input("Ingrese la cantidad de soles que desea vender: "))
            dollar = uno.venta(cantidad)
            print(f"La cantidad de dolares a recibir es: {dollar} ")
            input("Presione una tecla para volver al menu... ")
            borrarPantalla()
            continue
        if opcion == 4:
            borrarPantalla()
            continue
        if opcion == 5:
            break

    if opcion == 2:
        borrarPantalla()
        print(menuPokemon)
        opcion = int(input("Selecione una opcion: "))
        if opcion == 1:
            pokeVariable = pokeclas()
            pokeVariable.listar()
            input("Presione una tecla para volver al menu... ")
            borrarPantalla()
        if opcion == 2:
            data = pokedex()
            pokeVariable = pokeclas()
            nombre = input("Ingrese el nombre del pokemon: ")
            pokeVariable.buscar(nombre)
            input("Presione una tecla para volver al menu... ")
            borrarPantalla()
        if opcion == 3:
            borrarPantalla()
            continue   
        if opcion == 4:
            break

    if opcion == 3:
        break
'''

########################   EJERCICIO 4  ########################################

from Ejercicio4 import Registro
"""
objeto = Registro()
fecha = datetime.now()
objeto.guardar(fecha.strftime('%d/%m/%Y %H:%M:%S')+ " - Maestra"+" - Ella esta cansada\n")
objeto.guardar(fecha.strftime('%d/%m/%Y %H:%M:%S')+ " - Maestro"+" - Ella esta cansado\n")
objeto.guardar(fecha.strftime('%d/%m/%Y %H:%M:%S')+ " - Maestras"+" - Ella esta cansadas")
objeto.mostrar()
"""

########################   EJERCICIO 5  ########################################
import re 
from Ejercicio5 import ValidarNumero

numero = input("Ingrese el numero de telefono: ")
ValidarNumero(numero)