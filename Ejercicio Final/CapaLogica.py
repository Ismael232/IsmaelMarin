import pandas as pd
import uuid
from CapaModelo import *

def opcion(option):
    match option:
        case 1:
            ruta = input("Indique la ruta: ")
            rutaMejorada = r'{}'.format(ruta)
            hoja = input("Indique el nombre de la hoja: ")
            df = cargarArchivo(rutaMejorada,hoja)
            agregarPrecioTotal(df,hoja)
            print(df)
            return True
        case 2:
            nombreExcel = input("Escribe el nombre del archivo excel: ")
            dataframe = pd.read_excel(nombreExcel)
            nombreTabla = input("Escriba el nombre de la tabla a crear: ")
            insertDataToBase(nombreTabla,dataframe)
            print("La informacion de la base es: ")
            datos = showTable(nombreTabla)
            for filas in datos:
                print(filas)
            return True
        case 3:
            nombreTabla = input("Indique el nombre de la tabla donde se almacenara: ")
            createTable(nombreTabla)
            cantidad = int(input("Cuantas filas agregara? "))
            i = 0
            while i < cantidad:
                id = uuid.uuid4()
                idtext = str(id)
                print(f"USIARIO {i+1}\n")
                nombre = input("Escriba nombre de usuario: ")
                telefono = input("Ingrese el telefono: ")
                insertData(idtext,nombre,telefono,nombreTabla)
                i+=1
            return True

        case 4:
            return False
        case _:
            print("Opcion no valida")
            return True

def cargarArchivo(ruta,hoja):
    df_excel = pd.read_excel(ruta,sheet_name=hoja)
    return df_excel

def agregarPrecioTotal(dataframe,hoja):
    dataframe["PrecioTotal"] = dataframe["Unidades vendidas"] * dataframe ["Precio unitario"]
    rutaNueva = ".//PruebaCopia.xlsx"
    dataframe.to_excel(rutaNueva,sheet_name= hoja,encoding='utf-8',index = False)
