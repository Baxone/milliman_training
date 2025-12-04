# listas son conjuntos ordenados, mutables se puede modificar, y casi siempre suelen ser del mismo tipo.
lista_nombres = ['Nacho', 'Miguel', 'Igor', 'David']
lista = ['Carlos', 32, True]

# longitud
print(len(lista_nombres))  # 4

# imprimimos un elemento concreto, por posición empezamos en 0 y acabamos n-1 siendo n la longitud
print(lista_nombres[2])  # Igor

# recorrer todos los elementos de la lista
for nombre in lista_nombres:
    print(nombre)

# lista es un elemento mutable se puede modificar algo que exista.
lista_nombres[1] = 'Anais'
print(lista_nombres)

# se pueden añadir nuevos elementos a la lista al final de la lista
lista_nombres.append('Juan')
print(lista_nombres)
# se pueden añadir un elemento en cualquier posicion
lista_nombres.insert(3, 'Marika')
print(lista_nombres)
# se pueden insertar varios elementos a la vez
lista_nombres.extend(['Miguel', 'Javier', 'Lucia'])
print(lista_nombres)

# borrar elementos, pop() elimina elementos por el final, pop tambien permite eliminar en cualquier posicion pop(1), devuelve el elemento eliminado
ultimo_nombre = lista_nombres.pop()
print(ultimo_nombre)
print(lista_nombres)

lista_nombres.pop(5)  # juan se va, se puede usar indices negativos
print(lista_nombres)

lista_nombres.remove('anais'.title())
print('ana isabel'.capitalize())
print('ana isabel'.title())

# vaciar una lista
lista_nombres.clear()

# eliminar lista
del lista_nombres
