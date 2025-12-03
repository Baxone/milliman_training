numero_1 = 6
numero_2 = 12


def sumar(n1, n2):
    resultado = n1 + n2
    print(resultado)


sumar(1, 2)  # 3
sumar(12, 3)  # 15
sumar(numero_1, numero_2)  # 18


# los parametros pueden ser obligatorios y optativos. Primero todos los obligatorios y luego todos los optativos.
def saludar(name, surname='Rodriguez'):
    print(f'Hola me llamo {name} {surname}')


saludar('Juan')
saludar('Almudena', 'Frias')
saludar('Pepe', 'Villuela')
