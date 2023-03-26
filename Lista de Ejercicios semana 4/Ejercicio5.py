import re
def ValidarNumero(numero):
    patron = r'^9\d*$'
    if re.match(patron,numero):
        print("El numero es valido")
    else:
        print("El numero no es valido")