def sumar(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    print(suma)


sumar(1, 2)  # 3
sumar(2, 4, 6, 8)  # 20
sumar(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # 10


# funcion que me calcule la media de un conjunto de numero cualquiera.

def media(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    print(suma / len(numeros))


media(1, 2)  # 3
media(2, 4, 6, 8)  # 20
media(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # 10
