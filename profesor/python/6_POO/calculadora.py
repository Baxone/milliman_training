import math


class Calculadora:
    marca = ""
    bateria = False
    cientifica = False

    # la funcion no es obligatoria
    def __init__(self, marca: str, bateria: bool, cientifica=False):
        self.marca = marca
        self.bateria = bateria
        self.cientifica = cientifica

    def sumar(self, list_numeros: list[float]) -> float:
        return sum(list_numeros)

    def redondeo(self, numero: float, cantidad: int) -> float:
        return round(numero, cantidad)

    def raiz_cuadrada(self, numero: float):
        if not self.cientifica:
            return 'La calculadora no es cientifica'
        return math.sqrt(numero)

    def get_pi(self):
        return math.pi

    def logaritmo(self, numero: float):
        """Calcula el logaritmo en base 10 de `numero`.

        Retorna un mensaje si la calculadora no es científica o si el
        número no es válido (<= 0).
        """
        if not self.cientifica:
            return 'La calculadora no es cientifica'
        if numero <= 0:
            return 'El logaritmo no está definido para números <= 0'
        return math.log10(numero)
