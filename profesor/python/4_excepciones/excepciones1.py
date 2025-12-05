# una excepcion es un condicional disfrazado
# try -except
# try gestiona la parte correcta de mi resolución - except gestiona la parte incorrecta donde sale el error.
# https://docs.python.org/3/library/exceptions.html

def printNumbers():
    try:
        numero_1 = int(input('Dime un numero: '))
        numero_2 = int(input('Dime otro numero: '))
        print(numero_1, numero_2)
    except ValueError:
        print(
            'Has introducido un tipo de dato incorrecto, necesito que sean numeros enteros')
        printNumbers()
    except:
        print('Error generico')


printNumbers()
