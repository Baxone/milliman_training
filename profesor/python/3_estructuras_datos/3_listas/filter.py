lista_numeros = [1, 3, 4, 5, 6, 7, 3, 4, 5, 56,
                 73, 234, 5, 567, 32435, 7, 8, 54, 32, 1]

# sacar de la lista los numeros impares.

lista_impares = []
for numero in lista_numeros:
    if numero % 2 != 0:
        lista_impares.append(numero)

print(lista_impares)

# la lista de pares pero usando filter


def getPar(numero):
    return numero % 2 == 0


# lista_pares = list(filter(lambda numero: numero % 2 == 0, lista_numeros))
lista_pares = list(filter(getPar, lista_numeros))
print(lista_pares)


# casa o Perro
palabra = "casa"
otra_palabra = 'Perro'
print(palabra.upper())  # CASA
print(otra_palabra.lower())  # perro
print(palabra.capitalize())  # Casa
print(otra_palabra.lower().islower())

# En la palabra Reloj como se que la primera es mayuscula
mi_palabra = 'Reloj'
print(mi_palabra.istitle())

lista_animales = ['Leon', 'gato', 'perro',
                  'Cuervo', 'Aguila', 'Colibri', 'hipopotamo']

lista_animales_minuscula = list(
    filter(lambda animal: animal.islower(), lista_animales))
print(lista_animales_minuscula)


def getUpper(palabra):
    return palabra[0].isupper()


lista_animales_mayuscula = list(filter(getUpper, lista_animales))
print(lista_animales_mayuscula)
