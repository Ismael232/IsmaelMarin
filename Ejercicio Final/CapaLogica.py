import pandas as pd
from CapaModelo import *

def opcion(option):
    match option:
        case 1:
            ruta = input("Indique la ruta: ")
            rutaMejorada = r'{}'.format(ruta)
            hoja = input("Indique el nombre de la hoja: ")
            cargarArchivo(rutaMejorada,hoja)
        case 2:
            pass
        case 3:
            pass
        case _:
            print("Opcion no valida")

def cargarArchivo(ruta,hoja):
    df_excel = pd.read_excel(ruta,sheet_name=hoja)
    print(df_excel)


