def mostrar_resultado(resultado, n1, n2, tipo, error):
    if error == True:
        print('Calculo no valido')
    else:
        print(f'El resultado de {tipo} {n1} y {n2} es {resultado}')


def sumar(n1, n2): return n1 + n2


def restar(n1, n2): return n1 - n2


def multiplicar(n1, n2): return n1 * n2


def dividir(n1, n2): return n1 / n2


def calcular(n1, n2, tipo):
    resultado = 0
    error = False
    if tipo == 'sumar':
        resultado = sumar(n1, n2)
    elif tipo == 'restar':
        resultado = restar(n1, n2)
    elif tipo == 'multiplicar':
        resultado = multiplicar(n1, n2)
    elif tipo == 'dividir':
        resultado = dividir(n1, n2)
    else:
        error = True
    mostrar_resultado(resultado, n1, n2, tipo, error)
