'''para la pregunta 4 al importar la funciones usar el manejo de errores (try ,except) y en las
sentencias de “ else “ imprimir la ruta del directorio de trabajo os.getcwd() y en la sentencia
finally imprimir “proceso terminado”
'''
import os
try:
    from Ejercicio4 import Producto

except Exception as E:
    print(f"El error fue: {E}")

else:
    print(os.getcwd())
    
finally:
    print("Proceso terminado")


