# AULA 253

"""
Este e um modulo de exemplo

Este modulo contem funçoes e exemplos de documentaçao de funçoes.
A funçao soma voce ja conhece bastante
"""

variavel_1 = 1

def soma(x: int | float, y: int | float) -> int| float:
    """
    Soma x e y 

    :param x: Numero 1
    :type X: int or float
    :param y: Numero 2
    :type y: int or float

    :return: A soma entre x e y
    :rtype: int or float
    """
    return x + y

def multiplica(
        
        x: int | float,
        y: int | float,
        z: int | float | None = None
) -> int | float:
    """
    Multiplica x, y e/ou z

    Multiplica x e y. Se z for enviado, multiplica x, y, z.
    """
    if z is None:
        return x * y
    return x * y * z

variavel_2 = 2
variavel_3 = 3
variavel_4 = 4