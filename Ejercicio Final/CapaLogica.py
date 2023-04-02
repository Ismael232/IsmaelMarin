import pandas as pd
from CapaModelo import *

def opcion(option):
    match option:
        case 1:
            ruta = input("Indique la ruta: ")
            rutaMejorada = r'{}'.format(ruta)
            hoja = input("Indique el nombre de la hoja: ")
            df = cargarArchivo(rutaMejorada,hoja)
            decision = input("Desea agregar una columna de precio total?[s/n]")
            if decision.upper() == "S":
                agregarPrecioTotal(df,hoja)
            else:
                print("No se realizaron cambios")
            print(df)
        case 2:
            pass
        case 3:
            break
        case _:
            print("Opcion no valida")

def cargarArchivo(ruta,hoja):
    df_excel = pd.read_excel(ruta,sheet_name=hoja)
    print(df_excel)
    return df_excel

def agregarPrecioTotal(dataframe,hoja):
    dataframe["PrecioTotal"] = dataframe["Unidades vendidas"] * dataframe ["Precio unitario"]
    rutaNueva = ".//PruebaCopia.xlsx"
    dataframe.to_excel(rutaNueva,sheet_name= hoja,encoding='utf-8',index = False)
