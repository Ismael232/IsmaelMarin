
diccionario = {"nombreDeCurso": "","cantidadDeAlumnos": 0, "Activo": False, "NombreDelProfesor": "",
               "maxNota": 0, "Alumnos": []}
valor1 = input("Ingrese un valor para el nombre del curso: ")
diccionario["nombreDeCurso"] = valor1

valor2 = int(input("Ingrese la cantidad de alumnos: "))
diccionario["cantidadDeAlumnos"] = valor2

valor3 = input("Escriba el nombre del profesor: ")
diccionario["NombreDelProfesor"] = valor3

valor4 = int(input("Escriba la máxima nota: "))
diccionario["maxNota"] = valor4

valor5 = input("Escriba los nombres de los alumnos separados por un espacio: ")
diccionario["Alumnos"] = valor5.split(" ")
print(diccionario)