from datetime import datetime

def NombreEvento(nombre):
    listaEventos = ["Lolapolooza", "Rockfest","YoutuSummer"]
    for eventos in listaEventos:
        if nombre.upper() == eventos.upper():
            return True

def artistas(artista,nombre):
    listaArtistas = ["Marc Tomato", "Estefani Arias", "Renzo Oviedo"]
    for artistas in listaArtistas:
        if artista == "Marc Tomato" and nombre == "Lolapolooza":
            return True
        elif artista == "Estefani Arias" and nombre == "Rockfest":
            return True
        elif artista == "Renzo Oviedo" and nombre == "YoutuSummer":
            return True
        else:
            return False
        
def fechas(fecha, nombre):
    if nombre == "Lolapolooza" and fecha> datetime.strptime("14/01/2022","%d/%m/%Y") and fecha < datetime.strptime("25/02/2022", "%d/%m/%Y"):
        return True
    elif nombre == "Rockfest" and fecha> datetime.strptime("25/06/2022", "%d/%m/%Y") and fecha < datetime.strptime("27/08/2022", "%d/%m/%Y"):
        return True
    elif nombre == "YoutuSummer" and fecha> datetime.strptime("8/09/2022", "%d/%m/%Y") and fecha < datetime.strptime("15/09/2022", "%d/%m/%Y"):
        return True
    else:
        return False

def main():
    evento = input("Ingrese el nombre del evento: ")
    artista = input("Ingrese el nombre del artista a presentarse: ")
    fechaInicial = input("Ingrese la fecha del evento: ")
    fecha = datetime.strptime(fechaInicial,"%d/%m/%Y")
    if NombreEvento(evento) is True and artistas(artista,evento) is True and fechas(fecha,evento) is True:
        print("El evento es permitido")
    else:
        print("El evento no es permitido, por favor revise los requerimientos ")

main()