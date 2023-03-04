x = float(input("Ingrese el primer numero: "))
y = float(input("Ingrese el segundo numero: "))

if x == y:
        print(f"{x} es igual a {y}")
else:
    if x > y:
        print(f"{x} es mayor y diferente a {y}")
    else:
        print(f"{y} es mayor y diferente a {x}")