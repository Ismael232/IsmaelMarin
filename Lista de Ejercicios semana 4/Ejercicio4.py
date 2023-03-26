from datetime import datetime
class Registro:
    def __init__(self) -> None:
        self.archivo = open("texto.txt", "a")
    def guardar(self,contenido):
        self.archivo = open("texto.txt","a") 
        self.archivo.write(contenido)
        self.archivo.close()
    def mostrar(self):
        self.archivo = open("texto.txt","r")
        contenido = self.archivo.read()
        print(contenido)
        self.archivo.close()


