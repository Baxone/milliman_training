lista_nombres = ['Nacho', 'Miguel', 'Igor', 'David', 'Miguel', 'David']

# metodo que permite saber cuantas veces hay un elemento en lista. count()
print(lista_nombres.count('David'))
# copy() genera un copia de la lista para no modificar la original
lista_reverse = lista_nombres.copy()
# metodo para invertir un lista. Modifica la lista original
lista_reverse.reverse()
print(lista_reverse)
print(lista_nombres)

# copia de la lista desdes la posicion 2 hasta la 5 sin incluir la ultima
list_corta = lista_nombres[2:5]

# ordenar lista sort() modifica la lista original
numeros = [12, 33, 45, 6, 47, 345, 89]
letras = ['a', 'F', 'D', 'i', 'b']

numeros.sort()
print(numeros)
letras.sort(key=str.lower, reverse=True)
print(letras)
letras.sort(key=lambda letra: (letra.isupper(), letra.lower()))
print(letras)

# MAX y MIN saca el numero maximo y minimo
print(max(numeros))
print(min(numeros))
