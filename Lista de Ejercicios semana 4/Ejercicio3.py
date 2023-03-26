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

class pokeclas:
    data = pokedex()
    def listar(self):
        lista = self.data['pokemon_entries']
        for i,value in enumerate(lista):
            nombre = value['pokemon_species']['name']
            print(i,")",nombre)
    def buscar(self,nombre):
        lista = self.data['pokemon_entries']
        for i,valor in enumerate(lista):
            if valor['pokemon_species']['name'] == nombre:
                    print("¡Esta en la lista!")
                    print(valor['pokemon_species']['name'], ",enlace: ",valor['pokemon_species']['url'])
                    condicion = False
                    break
            else:
                    condicion = True
        if condicion:
                print("El pokemon no esta en la lista")
