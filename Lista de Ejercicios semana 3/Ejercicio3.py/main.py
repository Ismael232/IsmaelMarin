from model import division

x = float(input("Numerador: "))
y = float(input("Denominador: "))
if y != 0:
    resultado = division(x,y)
    print(resultado)
else:
    print("El denominador no puede ser 0")