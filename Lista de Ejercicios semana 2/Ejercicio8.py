def esPrimo(lista):
    primos = []
    for i in lista:
         if i == 1:
              pass
         aux = [*range(1,i+1)]
         count = 0
         for j in aux:
              if i%j == 0:
                   count += 1
         if count == 2:
            primos.append(i)
    return primos
                   
lista = [*range(1,1000)]

primos = esPrimo(lista)
print(primos)

