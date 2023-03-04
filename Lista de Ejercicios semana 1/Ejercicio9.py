
lista = [('Javier',45,'65245715'),('Rosa',25,'54214995'),('Hernan',65,'84552545'),('Lisa',14,'56223645')]
dnis = ['87895889', '57454154', '54214995', '14224575', '78489545', '54784564', '78785844', '84552545']
nombres = []
nuevaLista = []
i=0
while i<len(lista):
    if lista[i][1]>18 and lista[i][2] in dnis:
        nombres.append(lista[i][0])
        nuevaLista.append(lista[i])
    i += 1
print(f"Las personas que cumplen los requisitos son: {nombres}")
print(f"Elementos que cumplieron las condiciones: {nuevaLista}")
