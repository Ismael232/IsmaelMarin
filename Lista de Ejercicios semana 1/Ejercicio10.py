#0.Defina un diccionario que tenga las siguientes llaves (nombre de curso,cantidad
#de alumnos,activo(tipo boleano),nombre de profesor,max nota,alumnos(lista)) a
#todos ellos como valor que lleven un valor de inicializacion ,por ejemplo si es entero
#0 ,si es string una cadena vacia.
#-Realizar al menos 3 inputs para ingresar por teclado nuevos valores para el
#diccionario .
#-Imprimir el diccionario
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

valor5 = input("Escriba los nombres de los alumnos: ")
diccionario["Alumnos"] = valor5.split(" ")
print(diccionario)