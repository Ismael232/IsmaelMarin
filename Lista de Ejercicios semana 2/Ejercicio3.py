def mayorValor(x,y):
    if x>y:
        return x
    elif x<y:
        return y
    else:
        return "Los numeros son iguales"

x = int(input("Escriba el primer valor: "))
y = int(input("Escriba el segundo valor: "))

valor = mayorValor(x,y)
print(f"El mayor valor es {valor}")