from calculadora import Calculadora

casio = Calculadora('casio', True, True)
resultado_suma = casio.sumar([1, 2.3456, 3, 4.34567876987, 5])
print(casio.redondeo(resultado_suma, 3))
print(casio.raiz_cuadrada(256))
print(casio.get_pi())
