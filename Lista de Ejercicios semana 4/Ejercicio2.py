import random

class sorteo:
    lista = []
    def __init__(self,valorMax:float,cantidad:float) -> None:
        self.valorMax = valorMax
        self.cantidad  = cantidad
    
    def sorteoNumeros(self):
        for i in range(self.cantidad):
            self.lista.append(int(random.random()*self.valorMax+1))
if __name__ == "__main__":
    print("aaaaaaaaaaa")