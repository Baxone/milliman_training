def calcular():
    numero_1 = 0
    numero_2 = 0
    try:
        numero_1 = int(input('Dime un numero: '))
        numero_2 = int(input('Dime otro numero: '))
    except ValueError:
        print('Los valores introducidos no son numeros enteros')
        calcular()

    try:
        resultado = numero_1/numero_2
        print(resultado)
    except ZeroDivisionError:
        print('No se puede dividor por cero')
        calcular()


calcular()
