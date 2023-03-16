def ingresarNuevoLibro():
    estados = ["PRESTADO", "DISPONIBLE"]
    while True:
        nombreLibro = input("Ingrese nombre del libro: ")
        autor = input("Ingrese el autor del libro: ")
        categoria = input("Ingrese la categoria del libro: ")
        estado = input("Ingrese estado del libro: ")
        while True:
            if estado.upper() in estados:
                break
            else:
                estado = input("Escriba un estado disponible: ")
        nuevoDato ={
            "nombreLibro": nombreLibro ,
            "autor": autor,
            "categoria": categoria,
             "estado": estado
        }
        biblioteca["libro"].append(nuevoDato)
        respuesta = input("Desea agregar mas datos? [Si/No]: ")
        if respuesta.upper() == "NO":
            break
        
def ingresarNuevoUsuario():
    while True:
        nombre = input("Escriba el nombre de usuario: ")
        estado = input("¿Ha usado el servicio de prestamo? [Si/No]: ")
        nuevoDato = {
            "nombreUsuario": nombre,
            "estadoUsuario": estado
        }
        biblioteca["usuario"].append(nuevoDato)
        respuesta = input("Desea agregar mas datos? [Si/No]: ")
        if respuesta.upper() == "NO":
            break


def listaCategorias():
    listCategoria = []
    for libro in biblioteca["libro"]:
        listCategoria.append(libro["categoria"])
    print(listCategoria)

def listaNombreAutores():
    listNombreAutores = []
    for libro in biblioteca["libro"]:
        listNombreAutores.append([libro["nombreLibro"],libro["autor"]])
    print(listNombreAutores)

def cambioDeEstado():
    nombreLibro = input("Escriba el nombre del libro: ")
    for libro in biblioteca["libro"]:
        if nombreLibro in libro["nombreLibro"]:
            estado = libro["estado"] 
            respuesta = input(f"El libro se ecuentra en estado {estado}, ¿desea cambiarlo?: ")
            if respuesta.upper() == "SI":
                if estado.upper() == "PRESTADO":
                    libro["estado"] = "DISPONIBLE"
                else:
                    libro["estado"] = "PRESTADO"
                print("Se realizaron los cambios")
                print(libro)
            else:
                print("No se realizaron cambios")
        else:
            pass

def listaUsuarios():
    listaUsuarios = []
    for usuarios in biblioteca["usuario"]:
        listaUsuarios.append(usuarios["nombreUsuario"])
    print(listaUsuarios)

biblioteca = {"nombre":"Biblioteca",
              "libro": [
                {"nombreLibro": "NA" ,
                "autor": "Desconocido",
                "categoria": "NA",
                 "estado": "NA" }
              ],
              "usuario":[
                {
                   "nombreUsuario": "NA",
                   "estadoUsuario": "NA",
                }
              ],
              "listaDeCategorias": listaCategorias,
              "listaNombreAutores": listaNombreAutores,
              "cambioDeEstado": cambioDeEstado,
              "listaUsuarios": listaUsuarios
              }



#ingresarNuevoLibro()
#listaCategorias()
#listaNombreAutores()
#cambioDeEstado()
#ingresarNuevoUsuario()
#listaUsuarios()