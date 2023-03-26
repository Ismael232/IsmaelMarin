import requests



def sunat():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
    data = requests.get(url).json()
    return data

def pokedex():
    url = "https://pokeapi.co/api/v2/pokedex/1/"
    data = requests.get(url).json()
    return data

def pokemon():
    url = "https://pokeapi.co/api/v2/pokemon/"
    data = requests.get(url).json()

class casaCambio:
    data = sunat()
    compraActualizado = data["compra"]
    ventaActualizado = data["venta"]
    def compra(self,cantidadDollar):
        cantidadSoles = cantidadDollar*self.compraActualizado
        return cantidadSoles
    def venta(self,cantidadSoles):
        cantidadDollar = cantidadSoles/self.ventaActualizado
        return cantidadDollar