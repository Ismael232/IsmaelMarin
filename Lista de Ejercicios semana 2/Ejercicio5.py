import os
def archivosDeTuCarpeta(path):
    aux = os.listdir(path)
    for arch in aux:
        rutaArchivos = os.path.join(path,arch)
        if os.path.isdir(rutaArchivos) is False:
           print(arch)
        else:
            archivosDeTuCarpeta(rutaArchivos)


direccion = input("Ingrese la direccion de la carpeta: ")
## Se agrega el valor r para concatenarlo a nuestra direccion
direccionMejorada = r'{}'.format(direccion)  
## Se usa este metodo ya que el programa no entiende bien la barra
#la barra invertida \, y con esto hacemos entender que esa barra no sea ningun comando solo texto y
#podemos poner nuestra ruta normalmente
archivosDeTuCarpeta(direccionMejorada)