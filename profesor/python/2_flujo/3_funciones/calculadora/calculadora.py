# la calculadora pedirá dos numeros por pantalla y un tipo de calculo (sumar, restar, multiplicar) y imprimira el resultado por pantalla.
# opcion 1. importar el fichero completo
# import lib.functions as fn
# opcion 2. importar solo aquellas funcionalidades del fichero que necesito
from lib.functions import calcular


def main():
    numero_1 = float(input('Dime el primer numero: '))
    numero_2 = float(input('Dime el segundo numero: '))
    tipo = input('Dime el tipo de calculo: ')
    calcular(numero_1, numero_2, tipo)


if __name__ == "__main__":
    main()
