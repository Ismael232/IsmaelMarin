import requests
def sunat():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
    data = requests.get(url).json()

def pokemon():
    url = "https://pokeapi.co/api/v2/pokedex/1/"
    data = requests.get(url).json()
    print(data)

url = "https://pokeapi.co/api/v2/pokemon"
data = requests.get(url).json()
print(data)