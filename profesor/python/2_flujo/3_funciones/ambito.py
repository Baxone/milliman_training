# el ambito en python es funcional . una variable es local solo dentro de un funcion y global fuera de cualquier funcion

frase = "El resultado es:"  # global no esta declarada dentro de una funcion
age = 0

if frase != "":
    age = 23  # global


def potencia(base, exponente):
    resultado = base ** exponente  # local
    return resultado


potencia_resultado = potencia(4, 2)
