# docstrings
def potencia(base: float, exponente: int) -> float:
    """
    Calcula la potencia de una base elevada a un exponente entero.

    Parameters
    ----------
    base : float
        Base numérica a elevar.
    exponente : int
        Exponente entero al que se eleva la base.

    Returns
    -------
    float
        Resultado de elevar la base al exponente (base ** exponente).

    Raises
    ------
    TypeError
        Si 'exponente' no es un entero o 'base' no es un número válido.
    """
    return base**exponente


def sumar(n1: int, n2: int) -> int:
    """
    Suma dos enteros.

    Args:
        n1 (int): Primer sumando.
        n2 (int): Segundo sumando.

    Returns:
        int: Resultado de la suma de n1 y n2.
    """
    return n1 + n2


def main():
    sumar(12, 2)


if __name__ == '__main__':
    main()
